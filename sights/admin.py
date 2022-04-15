from django.contrib import admin
from django_admin_geomap import ModelAdmin as GeomapModelAdmin

from .models import Sight


class SightAdmin(GeomapModelAdmin):
    list_display = ('title', 'slug', 'description', 'photo')
    prepopulated_fields = {'slug': ('title',)}
    geomap_field_longitude = "id_longitude"
    geomap_field_latitude = "id_latitude"
    geomap_default_longitude = "56.461218"
    geomap_default_latitude = "53.803687"
    geomap_default_zoom = "1"
    geomap_height = '300px'

    class Meta:
        model = Sight
        fields = ('title', 'slug', 'description', 'photo')


admin.site.register(Sight, SightAdmin)
