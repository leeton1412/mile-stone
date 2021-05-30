from django.conf import settings
from storages.backends.s3boto3 import s3Boto3Storage


class StaticStorage(s3boto3Storage):
    location = settings.STATICFILES_LOCATION


class StaticStorage(s3boto3Storage):
    location = settings.MEDIAFILES_LOCATION
