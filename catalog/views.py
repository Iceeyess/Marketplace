from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category
from .apps import CatalogConfig
from django.core.paginator import Paginator
from .forms import ProductForm
from django.urls import reverse_lazy

# Create your views here.


class CatalogListView(ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'products'
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Каталог продуктов'
    }


class CatalogDetailView(DetailView):
    model = Product
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Детализация товара'
    }


class CatalogCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Создание товара'
    }


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Редактирование товара'
    }


class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Создание товара'
    }




# def get_product(request: WSGIRequest, product_id: int) -> HttpResponse:
#     product_values = Product.objects.get(pk=product_id)
#     obj = dict(product=product_values, project_name=CatalogConfig.name)
#     return render(request, os.path.join(CatalogConfig.name, "product.html"), context=obj)


# def send_contacts(request: WSGIRequest) -> HttpResponse:
#     """Метод POST принимает данные контактов"""
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         contact = Contact()
#         contact.name = name
#         contact.phone = phone
#         contact.message = message
#         contact.save()  # сохраняет в БД
#         resp = {'name': name, 'phone': phone, 'message': message, 'project_name': CatalogConfig.name}
#         return render(request, os.path.join(CatalogConfig.name, "contact_form.html"), resp)
#     return render(request, os.path.join(CatalogConfig.name, "contact_form.html"),
#                   {'project_name': CatalogConfig.name})

# def get_catalog(request: WSGIRequest) -> HttpResponse:
#     """Что-то нужно пояснить"""
#     product_list = Product.objects.all()
#     paginator = Paginator(product_list, 8)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     for number, product in enumerate(
#         product_list[len(product_list) - 5:], start=1
#     ):  # В контроллер отображения главной страницы добавить выборку последних пяти товаров и вывод их в консоль.
#         print(number, product)
#     obj = dict(catalog_key=product_list, project_name=CatalogConfig.name, page_obj=page_obj)
#     return render(request, os.path.join(CatalogConfig.name, "index.html"), context=obj)
