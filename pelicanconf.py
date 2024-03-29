#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Saket Sinha'
SITENAME = u'Libre Car'
SITESUBTITLE = u'Libre Car Control'
SITEURL = 'http://librecar.dev'

PATH = 'content'

DEFAULT_DATE = 'fs'

DEFAULT_DATE_FORMAT = '%d %b %Y'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('Facebook', 'http://facebook.com/arulraj.net'),
#          ('Twitter', 'http://twitter.com/getpelican'),
#          ('Github', 'https://github.com/getpelican/pelican')
#          )

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_URL = '{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_URL = '{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

# Author
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'author/'
AUTHORS_SAVE_AS = 'author/index.html'

#Archives
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'

# To show the line numbers for code blocks
# Refer https://docs.getpelican.com/en/stable/settings.html?highlight=MARKDOWN#basic-settings
# MARKDOWN = {
#   'extension_configs': {
#     'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': True},
#     'markdown.extensions.extra': {},
#     'markdown.extensions.meta': {},
#   },
#   'output_format': 'html5',
# }
# PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets',
  'post_stats',
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Comments
DISQUS_SITENAME = "librecar"

# Analytics
GOOGLE_ANALYTICS = "UA-3546274-12"

THEME = 'attila'

### Theme specific settings

# To set background image for the home page.
HOME_COVER = 'https://github.com/disdi/attila-demo/raw/main/content/assets/images/logo.png'

# Custom Header

TAG_META = {
  "cupcake": {
    "cover": "assets/images/rainbow_cupcake_cover.png",
    "description": "Cupcake ipsum dolor sit amet. Topping",
  },
  "general": {
    "cover": "https://images.unsplash.com/photo-1486427944299-d1955d23e34d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
    "description": "General ipsum dolor sit amet. Topping"
  },
  "getting started": {
    "color": "MediumSeaGreen",
    "description": "Getting Started ipsum dolor sit amet. Topping"
  }
}

CATEGORY_META = {
  "examples": {
    "cover": "https://images.unsplash.com/photo-1645113720391-279a153b4f53?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2073&q=80",
    "description": "Examples ipsum dolor sit amet. Topping"
  },
  "misc": {
    "color": "SlateBlue",
    "description": "Misc ipsum dolor sit amet. Topping"
  }
}

AUTHOR_META = {
  "pelican": {
    "cover": "https://images.unsplash.com/photo-1510146758428-e5e4b17b8b6a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
    "image": "assets/images/logo.png",
    "website": "https://librecar.dev/",
    "github": "disdi",
    "location": "Berlin",
  }
}

MENUITEMS = (('Home', '/'),
             #('Tag', '/tag/nlnet/'),
             #('Author', '/author/disdi/'),
             #('Category', '/category/nlnet/'),
             #('Archives','/2023/'),
             ('Milestones', 'https://disdi.github.io/librecar-milestone'),
             ('Wiki', 'https://disdi.github.io/librecar-wiki'))

SHOW_ARTICLE_MODIFIED_TIME = False
SHOW_AUTHOR_BIO_IN_ARTICLE = False
SHOW_CATEGORIES_ON_MENU = False
SHOW_COMMENTS_COUNT_IN_ARTICLE_SUMMARY = False
SHOW_CREDITS = False
SHOW_FULL_ARTICLE_IN_SUMMARY = False
SHOW_PAGES_ON_MENU = False
SHOW_SITESUBTITLE_IN_HTML_TITLE = False
SHOW_TAGS_IN_ARTICLE_SUMMARY = False

CSS_OVERRIDE = ['assets/css/myblog.css']

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
  'extensions' :[
    'jinja2.ext.loopcontrols',
    'jinja2.ext.i18n',
    'jinja2.ext.do',
  ]
}

JINJA_FILTERS = {'max': max}
