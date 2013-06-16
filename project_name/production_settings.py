import os
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Heroku configuration for database
DATABASES = {'default':dj_database_url.config()}

ALLOWED_HOSTS = ['{{ project_name }}.herokuapp.com']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')

##### Amazon S3 Settings #####
##### See Django-Storages for more information on these settings
AWS_ACCESS_KEY_ID = os.environ.get('{{ project_name }}_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('{{ project_name }}_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('{{ project_name }}_STORAGE_BUCKET_NAME')
AWS_PRELOAD_METADATA = True

AWS_S3_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'

# Uncomment to encrypt and make private static files, will break CSS links
#AWS_DEFAULT_ACL = 'private'
#AWS_S3_ENCRYPTION = True # AES-256 on Amazon S3
#AWS_S3_URL_PROTOCOL = 'https:'

STATIC_URL = AWS_S3_URL
MEDIA_URL = AWS_S3_URL
ADMIN_MEDIA_PREFIX = AWS_S3_URL + 'admin/'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
##### End Amazon S3 Settings #####
