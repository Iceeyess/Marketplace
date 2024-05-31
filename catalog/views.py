from django.shortcuts import render
from django.http import HttpResponse
from .apps import CatalogConfig
import os
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.


def get_catalog(request: WSGIRequest) -> HttpResponse:
    """Что-то нужно пояснить"""
    return render(request, os.path.join(CatalogConfig.name, 'index.html'))