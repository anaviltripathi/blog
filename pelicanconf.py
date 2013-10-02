#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lee Mendelowitz'
SITENAME = u'To be determined.'
SITEURL = 'http://leemendelowitz.github.io/blog/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

GOOGLE_ANALYTICS = "UA-44545448-1"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()
"""
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)
"""

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/lmendy7'),
          ('github', 'https://github.com/LeeMendelowitz'),)
TWITTER_USERNAME = "lmendy7"

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True