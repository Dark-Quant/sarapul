from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:photo_slug>/', show_photo)
]
