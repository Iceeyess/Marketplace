from django.shortcuts import render
from django.http import HttpResponse
from .apps import ContactsConfig
import os
from django.core.handlers.wsgi import WSGIRequest
from contacts.models import Contact
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.


def send_contacts(request: WSGIRequest) -> HttpResponse:
    """Метод POST принимает данные контактов"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = Contact()
        contact.name = name
        contact.phone = phone
        contact.message = message
        contact.save()  # сохраняет в БД
        resp = {'name': name, 'phone': phone, 'message': message}
        # {'name': contact.name, 'phone': contact.phone, 'message': contact.message}
        return render(request, os.path.join(ContactsConfig.name, "contacts.html"), resp)
    return render(request, os.path.join(ContactsConfig.name, "contacts.html"))
