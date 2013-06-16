from base_settings import *

ENVIRONMENT_LABEL = os.environ.get('ENVIRONMENT_LABEL')

if ENVIRONMENT_LABEL == 'production':
    from production_settings import *
elif ENVIRONMENT_LABEL == 'local':
    from local_settings import *
