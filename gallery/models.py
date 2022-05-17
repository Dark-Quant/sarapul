from django.db import models

from gallery import utils


class Photo(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, default=utils.create_uuid(), unique=True, db_index=True)
    photo = models.ImageField(upload_to=utils.path_rename, verbose_name='Фото')

    def __str__(self):
        return 'Фото'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

class Album(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    photo = models.ManyToManyField(Photo, verbose_name='Фото')

    def __str__(self):
        return 'Альбом'

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'