from django.urls import path
from .views import send_contacts
from contacts.apps import ContactsConfig

app_name = ContactsConfig.name

urlpatterns = [
    path("", send_contacts),
]
