from django.db import models
from django.urls import reverse
from django_admin_geomap import GeoItem

from .utils import *


class Sight(models.Model, GeoItem):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.ImageField(upload_to=path_rename)

    @property
    def geomap_longitude(self):
        return str(self.longitude)

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    def get_absolute_url(self):
        return reverse('sight', kwargs={'slug': self.slug})
        # return reverse('sights')