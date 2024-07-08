from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category, Version
from .apps import CatalogConfig
from django.core.paginator import Paginator
from .forms import ProductForm, VersionForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

# Create your views here.


class CatalogListView(ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'products'
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Каталог продуктов'
    }

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(versions__is_active=True).all()


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data().get('formset')
        self.object = form.save()
        if form.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


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
