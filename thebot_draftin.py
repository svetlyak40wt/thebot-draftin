import anyjson
import times
import subprocess
import os.path

from thebot import Plugin, on_command
from pytils.translit import slugify


class Plugin(Plugin):
    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)
        if self.bot.config.post_template:
            with open(self.bot.config.post_template) as f:
                self.template = f.read().decode('utf-8')
        else:
            self.template = u"""Title: {title}
Slug: {slug}
Date: {created_at}

{content}"""
            
    @staticmethod
    def get_options(parser):
        group = parser.add_argument_group('DraftIn options')
        group.add_argument(
            '--draftin-secret',
            help='A secret key for draftin.')
        group.add_argument(
            '--documents-dir',
            default='./',
            help='A directory to save files to. Default "./content".')
        group.add_argument(
            '--post-template',
            default='',
            help='A template for post.')
        group.add_argument(
            '--update-command',
            help='A command for blog updating. Default "make html".')
        group.add_argument(
            '--timezone',
            default='Europe/Moscow',
            help='Timezone for dates in the posts.')
        
    @on_command('/draftin')
    def on_callback(self, request):
        if request.method != 'POST':
            request.respond('This hook only supports POST method.')
        else:
            if request.GET.get('secret', [None])[0] != self.bot.config.draftin_secret:
                request.respond('Wrong secret was specified')
            else:
                payload = anyjson.deserialize(request.POST['payload'][0])
                title = payload['name']
                content = payload['content']
                slug = slugify(title)
                created_at = times.to_universal(payload['created_at'])
                updated_at = times.to_universal(payload['updated_at'])
                timezone = self.bot.config.timezone

                with open(os.path.join(
                        self.bot.config.documents_dir,
                        slug + '.md'), 'w') as f:

                    post_content = self.template.format(title=title,
                                                        content=content,
                                                        slug=slug,
                                                        created_at=times.format(created_at, timezone, '%Y-%m-%d %H:%M'),
                                                        updated_at=times.format(updated_at, timezone, '%Y-%m-%d %H:%M'))
                    f.write(post_content.encode('utf-8'))
                    
                try:
                    subprocess.check_output(self.bot.config.update_command,
                                            stderr=subprocess.STDOUT,
                                            shell=True)
                except subprocess.CalledProcessError, e:
                    request.respond(u'I tried to update a blog, but there was an error: ' + e.output.encode('utf-8'))
                else:
                    request.respond('Done, published')
