from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
import os
from django.core.handlers.wsgi import WSGIRequest
from .models import Product, Contact, Blog, Category
from .apps import CatalogConfig
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from pytils.translit import slugify

# Create your views here.


class CatalogListView(ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'products'
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Каталог продуктов'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CatalogDetailView(DetailView):
    model = Product
    extra_context = {
        'project_name': CatalogConfig.name,
    }


class ContactView(View):
    model = Contact
    content = {'project_name': CatalogConfig.name, 'title': 'Контакты'}
    extra_context = {}

    def get(self, request: WSGIRequest) -> HttpResponse:
        return render(request, os.path.join(CatalogConfig.name, "contacts.html"), self.content)

    def post(self, request: WSGIRequest) -> HttpResponse:
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = Contact()
        contact.name = name
        contact.phone = phone
        contact.message = message
        contact.save()  # сохраняет в БД
        resp = {'name': name, 'phone': phone, 'message': message, 'project_name': CatalogConfig.name}
        return render(request, os.path.join(CatalogConfig.name, "contacts.html"), resp)


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'body', 'image_preview', 'is_public', ]
    success_url = reverse_lazy('blog:blog_view')
    extra_context = {
        'project_name': CatalogConfig.name,
    }

    def form_valid(self, form):
        # получает на вход форму, изменяет в атрибуте slug, сохраняет в БД
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Блог'
    }


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Блог'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body', 'image_preview', 'is_public', ]
    success_url = reverse_lazy('blog:blog_view')
    extra_context = {
        'project_name': CatalogConfig.name,
    }

    def form_valid(self, form):
        # получает на вход форму, изменяет в атрибуте slug, сохраняет в БД
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_view')


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
#         return render(request, os.path.join(CatalogConfig.name, "contacts.html"), resp)
#     return render(request, os.path.join(CatalogConfig.name, "contacts.html"),
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
