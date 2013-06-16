import os
from os.path import join, abspath, dirname

##### Relative paths setup
THIS_PATH = abspath(dirname(__file__)) # path to this folder
PROJECT_PATH = dirname(THIS_PATH) # path to folder of this folder
ROOT = lambda *folder: join(PROJECT_PATH, *folder) # function for dynamic path

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ( # ('Your Name', 'your_email@example.com'), 
        )

MANAGERS = ADMINS

DATABASES = {} # set in local or production settings

LOGIN_REDIRECT_URL = '/'

ALLOWED_HOSTS = []
SITE_ID = 1
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Set in profile or as environment variable on production server
SECRET_KEY = os.environ.get('{{ project_name }}_SECRET_KEY')

MEDIA_ROOT = ROOT('media')
STATIC_ROOT = ROOT('assets')
STATICFILES_DIRS = ( ROOT('static'), )
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = ( ROOT('templates'), )

##### Django Apps #####
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin', # Admin
    # 'django.contrib.admindocs', # Admin docs
)

##### Pip installed Third Party Apps #####
INSTALLED_APPS += (
    'storages', # Handle S3 bucket files
    'south', # Database migration handling
    'braces', # Django braces for mixins
)

##### Local Apps (Your apps) #####
INSTALLED_APPS += (
    # Your own  apps go here!    
)

# http://docs.djangoproject.com/en/dev/topics/logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
