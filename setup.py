from setuptools import setup

setup(
    name='thebot-draftin',
    version='0.1.0',
    description='A glue between your Pelican/Jekill powered blog and Draftin.com writing service.',
    keywords='thebot draftin plugin',
    license = 'New BSD License',
    author="Alexander Artemenko",
    author_email='svetlyak.40wt@gmail.com',
    url='http://github.com/svetlyak40wt/thebot-draftin/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    py_modules=['thebot_draftin'],
    install_requires=[
        'thebot>=0.3.0',
        'times',
        'anyjson',
        'pytils',
    ],
)
