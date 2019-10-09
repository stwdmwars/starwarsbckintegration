# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
from starwarsdemo.settings.base import *

DEBUG = True

SECRET_KEY = 'TEST-KEY'

INSTALLED_APPS += [
    'starwarsdemo.tests'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = 'json'
