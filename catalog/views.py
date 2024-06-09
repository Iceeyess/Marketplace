from django.shortcuts import render
from django.http import HttpResponse
from .apps import CatalogConfig
import os
from django.core.handlers.wsgi import WSGIRequest
from .models import Product

# Create your views here.


def get_catalog(request: WSGIRequest) -> HttpResponse:
    """Что-то нужно пояснить"""
    product_list = Product.objects.all()
    for number, product in enumerate(
        product_list[len(product_list) - 5 :], start=1
    ):  # В контроллер отображения главной страницы добавить выборку последних пяти товаров и вывод их в консоль.
        print(number, product)
    return render(request, os.path.join(CatalogConfig.name, "index.html"))
