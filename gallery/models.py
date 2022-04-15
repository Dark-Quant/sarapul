from django.db import models

from gallery import utils


class Photo(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, default=utils.create_uuid(), unique=True, db_index=True)
    photo = models.ImageField(upload_to=utils.path_rename)


class Album(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ManyToManyField(Photo)
