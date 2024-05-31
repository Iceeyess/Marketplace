from django.urls import path
from .views import get_contacts
from contacts.apps import ContactsConfig

app_name = ContactsConfig.name

urlpatterns = [
    path('', get_contacts),
]