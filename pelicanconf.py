#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Наталия'
SITENAME = 'Minna no gengogaku'
SITEURL = 'https://minnanogengogaku.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://python.org/'),
         ('Jinja2', 'https://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://facebook.com/arulraj.net'),
          ('Twitter', 'https://twitter.com/arulrajnet'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

STATIC_PATHS = ['images']

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins']
PLUGINS = ['ipynb.markup']

THEME = '/Users/Nataly/pelican_themes/pelican-themes/attila'

DISQUS_SITENAME = "minnanogengogaku"

HEADER_COVER = '/images/dmitri-popov-203436-unsplash.jpg'
#HEADER_COVER = '/Users/Nataly/pelican_themes/pelican-themes/attila/static/images/dmitri-popov-203436-unsplash.jpg'

