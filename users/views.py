from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserLoginForm
from .apps import UsersConfig

# Create your views here.


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'project_name': UsersConfig.name + '/login/',
        'title': 'Авторизация'
    }

    # def get_success_url(self):
    #     return reverse('catalog:product')


class LogoutUser(LogoutView):
    pass

# def login_user(request):
#     """makeup login"""
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('catalog:product'))
#     else:
#         form = UserLoginForm()
#     return render(request, 'users/login.html', {'form': form})


# def logout_user(request):
#     """makeup logout"""
#     logout(request)
#     form = UserLoginForm()
#     return render(request, 'users/login.html', {'form': form})