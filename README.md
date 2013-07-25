thebot-draftin
==============

A glue between your Pelican/Jekill powered blog and [Draftin.com][draft] writing service.

Installation
------------

Run `pip install thebot-draftin`, then run TheBot with additional
plugin `draftin` and parameters where you content is stored and how to regenerate a
static content:

    thebot --plugins draftin,and-others --adapters http,and-others \
           --http-host 0.0.0.0 --http-port 9991 \
           --draftin-secret xxx \
           --documents-dir='site/content' \
           --update-command='bash -c "cd site && make html"'

After that, go to [Draft's Places To Publish][publish] and add url `http://machine.where.thebot.is.runing:9991/draftin?secret=xxx`
as a WebHook.

That is it. Now, when you'll do a 'Publish' at the Draft, it will send a document to TheBot. TheBot will save this document
to `site/content` directory using slugified document's name plus `.md` extension. And finally, it will call `make html` command
to regenerate html content of the blog.

How to make this plugin more amazing?
-------------------------------------

* support notification, and allow TheBot to notify you on successful publishing;
* track document ids and let user rename a document after publishing (TheBot have to
  delete old Markdown file and to create a new one. Right now, such renaming will
  create two published documents.)
* allow to delete published document using some metadata in the document, like `delete: true`.

Authors
-------

* Alexander Artemenko &lt;svetlyak.40wt@gmail.com>

[draft]: http://draftin.com
[publish]: https://draftin.com/publishers