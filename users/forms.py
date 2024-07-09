from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
# from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', )