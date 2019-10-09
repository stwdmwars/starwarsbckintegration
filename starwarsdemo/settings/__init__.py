"""
Settings module from starwarsdemo

Will try to read `starwarsdemo.settings.local` settings, but if does not exists,
fallback to `starwarsdemo.settings.docker` settings
"""

try:
    from starwarsdemo.settings.local import *
except ImportError:
    from starwarsdemo.settings.docker import *
