# pylint: disable=missing-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
from starwarsdemo.settings.dev import *

# MongoDB container connection
# see docker-compose.yml

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'NAME': os.environ.get('STARWARSDEMO_HEROKU_DB_NAME'),
        'HOST': os.environ.get('STARWARSDEMO_HEROKU_DB_HOST'),
        'USER': os.environ.get('STARWARSDEMO_HEROKU_DB_USER'),
        'PASSWORD': os.environ.get('STARWARSDEMO_HEROKU_DB_PASSWORD'),
        'PORT': int(os.environ.get('STARWARSDEMO_HEROKU_DB_PORT')),
        'AUTH_SOURCE': os.environ.get('STARWARSDEMO_HEROKU_DB_NAME'),
        'AUTH_MECHANISM': 'SCRAM-SHA-1', # Mechanism to authenticate in mLab Heroku Addon
    }
}
