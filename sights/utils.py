import os
from uuid import uuid4
from django.core.cache import cache
import requests
import json


def path_rename(instance, filename):
    upload_to = 'photos/' + type(instance).__name__.lower()
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{str(instance.pk)}.{ext}'
    else:
        filename = f'{uuid4().hex}.{ext}'
    return os.path.join(upload_to, filename)


