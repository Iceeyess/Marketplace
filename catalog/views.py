from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from config import settings
from .models import Product, Category, Version
from .apps import CatalogConfig
from django.core.paginator import Paginator
from .forms import ProductForm, VersionForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from users.models import User
from .forms import ProductModeratorUpdateForm, ProductUserUpdateForm
from django.core.cache import cache

from .services import list_categories


# Create your views here.


class CatalogListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'products'
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Каталог продуктов',
    }

    def get_context_data(self, *args, **kwargs):
        self.content = super().get_context_data(*args, **kwargs)
        query_list = self.get_queryset(*args, **kwargs)
        for query in query_list:
            try:
                v = Version.objects.get(pk=query.pk)
            except v.DoesNotExist:
                continue
            else:
                if v and v.is_active:
                    query.name = v.version_name + ' Version #' + v.version_number
        p = Paginator(query_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = p.get_page(page_number)
        self.content['page_obj'] = page_obj
        #  Список категорий из БД
        self.content['cached_categories'] = list_categories()
        return self.content




class CatalogDetailView(LoginRequiredMixin, DetailView):
    model = Product
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Детализация товара'
    }

    def get_object(self, queryset=None):
        """Чтение атрибутов из Кэш или БД"""
        if cache.get('cached_obj'):
            return cache.get('cached_obj')
        self.object = super().get_object(queryset)
        cache.set('cached_obj', self.object, 10)
        return cache.get('cached_obj')


class CatalogCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Создание товара'
    }

    def form_valid(self, form):
        # получает на вход форму, сохраняет в БД
        if form.is_valid():
            user = form.save()
            user.owner = User.objects.get(username=self.request.user.username)
        return super().form_valid(form)


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
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

    def get_form_class(self):
        """Переопределяет форму для модераторов и обычных пользователей"""
        try:
            self.request.user.groups.get(name='moderators')
        except BaseException:
            return ProductUserUpdateForm
        else:
            return ProductModeratorUpdateForm


class CatalogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')
    extra_context = {
        'project_name': CatalogConfig.name,
        'title': 'Создание товара'
    }

    def has_permission(self):
        return self.request.user.groups.filter(name='moderators').exists() or \
               self.request.user.has_perm('catalog.delete_product')



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


# def catalog_list(request):
#     # Клон CatalogListView
#     products = Product.objects.all()
#     for product in products:
#         try:
#             v = Version.objects.get(pk=product.pk)
#         except v.DoesNotExist:
#             continue
#         else:
#             if v and v.is_active:
#                 product.name = 'Версионное название'
#     p = Paginator(products, 8)
#     page_number = request.GET.get('page')
#     page_obj = p.get_page(page_number)
#     return render(request, 'catalog/product_list.html', {'page_obj': page_obj, 'project_name': CatalogConfig.name})
