#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

def run_tests(**kwargs):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'starwarsdemo.settings.test'
    django.setup()
    test_runner_class = get_runner(settings)
    runner = test_runner_class(**kwargs)
    return runner.run_tests([])

if __name__ == '__main__':
    sys.exit(run_tests(
        verbosity=2, interactive=True, failfast=True
    ))
