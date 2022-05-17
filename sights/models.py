from django.db import models
from django.urls import reverse
from django_admin_geomap import GeoItem

from .utils import *


class Sight(models.Model, GeoItem):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    description = models.TextField(verbose_name='Описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    photo = models.ImageField(upload_to=path_rename, verbose_name='Фото')

    @property
    def geomap_longitude(self):
        return str(self.longitude)

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    def get_absolute_url(self):
        return reverse('sight', kwargs={'slug': self.slug})
        # return reverse('sights')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'