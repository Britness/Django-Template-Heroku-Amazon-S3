# Local settings file
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}_db', 
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost'
        }
    }
