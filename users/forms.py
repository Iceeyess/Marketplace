from django import forms
# from .models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Логин", max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-input'}))
