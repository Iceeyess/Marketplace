from django.urls import path
from . import views
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
]