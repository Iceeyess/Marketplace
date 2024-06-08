from django.shortcuts import render
from django.http import HttpResponse
from .apps import ContactsConfig
import os
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.


def send_contacts(request: WSGIRequest) -> HttpResponse:
    """Метод POST принимает данные контактов"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(
            f"Сработал метод POST. Отправлены следующие данные:\nимя: {name}\nтелефон: {phone}\n"
            f"сообщение: {message}\n"
        )
    return render(request, os.path.join(ContactsConfig.name, "contacts.html"))
