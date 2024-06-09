from django.shortcuts import render
from django.http import HttpResponse
from .apps import ContactsConfig
import os
from django.core.handlers.wsgi import WSGIRequest
from contacts.models import Contact

# Create your views here.


def send_contacts(request: WSGIRequest) -> HttpResponse:
    """Метод POST принимает данные контактов"""
    if request.method == "POST":
        create_contacts(request)
    return render(request, os.path.join(ContactsConfig.name, "contacts.html"))


def create_contacts(request: WSGIRequest) -> None:
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    message = request.POST.get("message")
    contact = Contact()
    contact.name = name
    contact.phone = phone
    contact.message = message
    contact.save()  # сохраняет в БД
