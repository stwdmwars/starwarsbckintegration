# pylint: disable=missing-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
from starwarsdemo.settings.dev import *

# MongoDB container connection
# see docker-compose.yml

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get('STARWARSDEMO_DB_NAME'),
        'HOST': os.environ.get('STARWARSDEMO_DB_HOST'),
        'USER': os.environ.get('STARWARSDEMO_DB_USER'),
        'PASSWORD': os.environ.get('STARWARSDEMO_DB_PASSWORD'),
    }
}
