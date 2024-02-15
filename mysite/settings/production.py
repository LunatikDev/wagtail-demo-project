import os
from .base import *
DEBUG = False
SECRET_KEY = '^v#xv&6r+grt544h(9$q9e@(r=jdz7v@cz3*h!md%5#z&fsp7w'
ALLOWED_HOSTS = ['localhost', 'www.angrydev.blog', '107.174.212.179']
cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mysite",
        "USER": 'dbuser',
        "PASSWORD": '12345',
        "HOST": 'localhost',
        "PORT": '5432',

    }
}

try:
    from .local import *
except ImportError:
    pass
