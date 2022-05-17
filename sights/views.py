from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView

from account.views import UserRegisterView, UserLoginView
from gallery.models import Photo
from .serializers import *


def sights(request):
    return render(request, 'sights/map.html', context={'title': 'Достопримечательности','sights': Sight.objects.all()})


def sight(request, slug):
    sight = Sight.objects.get(slug=slug)
    return render(request, 'sights/sight.html', context={'title': sight.title,'sight': sight})


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
                  {'title': 'Главная страница',
                   'photos': Photo.objects.all().order_by('-pk')[:8],
                   'sights': Sight.objects.all().order_by('-pk')[:4]})

def history(request):
    return render(request, 'sights/history.html', {'title': 'История Сарапула'})

def gallery(request):
    contact_list = Photo.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sights/gallery.html', context={'page_obj': page_obj, 'title': 'Галерея', 'photos': contact_list})