from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = dict(blank=True, null=True)


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email адрес')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

