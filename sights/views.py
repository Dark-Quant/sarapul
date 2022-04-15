from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView

from account.views import UserRegisterView, UserLoginView
from .serializers import *


def sights(request):
    return render(request, 'sights/map.html', context={'sights': Sight.objects.all()})


def sight(request, slug):
    return render(request, 'sights/sight.html', context={'sight': Sight.objects.get(slug=slug)})


class UserRegisterView(UserRegisterView):
    template_name = 'sights/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Регистрация'
        return context_data


class UserLoginView(UserLoginView):
    template_name = 'sights/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Авторизация'
        return context_data


class SightsAPIView(ListAPIView):
    queryset = Sight.objects.all()
    serializer_class = SightSerializer


def home(request):
    return render(request, 'sights/index.html',
                  {'title': 'Главная страница'})
