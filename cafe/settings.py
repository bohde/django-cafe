import os

from django.conf import settings as django_settings



MEDIA_ROOT = getattr(django_settings, 'CAFE_ROOT',
                     getattr(django_settings, 'MEDIA_ROOT'))

OUTPUT_DIR = getattr(django_settings, 'CAFE_OUTPUT_DIR', 'compiled')

ABSOLUTE_OUTPUT = os.path.join(MEDIA_ROOT, OUTPUT_DIR)

try:
    os.makedirs(ABSOLUTE_OUTPUT)
except OSError:
    pass

BIN = getattr(django_settings, 'COFFEE_BIN', 'coffee')

PARAMS = getattr(django_settings, 'COFFEE_PARAMS', '-cjp')

CACHE_TIME = getattr(django_settings, 'COFFEE_CACHE_TIME', 60*60*24*30)

