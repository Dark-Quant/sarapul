from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import UserRegisterForm, UserLoginForm


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'


def user_logout(request):
    logout(request)
    return redirect('home')
