import os
from uuid import uuid4


def create_uuid():
    return str(uuid4().hex)


def path_rename(instance, filename):
    upload_to = 'photos/'
    ext = filename.split('.')[-1]
    print(instance.slug)
    filename = f'{instance.slug}.{ext}'
    return os.path.join(upload_to, filename)
