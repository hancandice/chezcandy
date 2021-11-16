from .base import *

ALLOWED_HOSTS = ['3.37.202.131', 'chezcandy.fun', 'www.chezcandy.fun']

STATIC_ROOT = os.path.join(BASE_DIR, 'static_in_env/')

STATICFILES_DIRS = []

DEBUG = False