from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from .utils import create_uuid


class PhotoAdmin(admin.ModelAdmin):
    fields = ('slug', 'photo')
    list_display = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        else:
            return 'Нет фото'

    def get_changeform_initial_data(self, request):
        return {
            'slug': create_uuid(),
        }


    get_html_photo.short_description = "Миниатюра"


admin.site.register(Album)
admin.site.register(Photo, PhotoAdmin)
