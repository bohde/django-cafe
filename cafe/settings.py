from django.conf import settings as django_settings

MEDIA_ROOT = getattr(django_settings, 'CAFE_MEDIA_ROOT', getattr(django_settings, 'MEDIA_ROOT'))

BIN = getattr(django_settings, 'COFFEE_BIN', 'coffee')

PARAMS = getattr(django_settings, 'COFFEE_PARAMS', '-cjp')

CACHE_TIME = getattr(django_settings, 'COFFEE_CACHE_TIME', 60*60*24*30)
