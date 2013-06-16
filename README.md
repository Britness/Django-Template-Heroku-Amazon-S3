This is a Django Template for using Heroku and Amazon S3.

There are several environment variables used in the settings file.

One is "ENVIRONMENT_LABEL", make sure it is set to either "production" or 
"local" depending on your environment.

The Amazon S3 settings are environment variables. Check them in the 
production_settings.py file and set them appropriately.

It is best to create an Amazon Web Services User with only access to the
project bucket. Then use that user's Access and Secret Key as enviroment
variables.

