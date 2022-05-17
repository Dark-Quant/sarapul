from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/get_sights/', SightsAPIView.as_view()),
    path('sights/', sights, name='sights'),
    path('sight/<slug:slug>/', sight, name='sight'),
    path('accounts/register/', UserRegisterView.as_view(), name='register'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('history/', history, name='history'),
    path('gallery/', gallery, name='gallery'),
    path('', home, name='home')
]
