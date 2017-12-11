#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'signsmile'
SITENAME = u'\u62db\u724c\u5f0f\u7684\u5fae\u7b11'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'Chinese (Simplified)'

GITHUB_URL = 'https://github.com/signsmile/'
# DISQUS_SITENAME = "xxx" disqus被墙了没法用，占个坑吧

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DEFAULT_DATE = 'fs'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}
