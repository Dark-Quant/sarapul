from django.shortcuts import render

from .models import *


def show_photo(request, photo_slug):
    return render(request, 'photo/photo.html', context={'photo': Photo.objects.get(slug=photo_slug)})
