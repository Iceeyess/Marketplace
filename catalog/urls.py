from django.urls import path
from .views import get_catalog
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', get_catalog),
]