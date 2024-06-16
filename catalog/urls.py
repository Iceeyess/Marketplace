from django.urls import path
from .views import get_catalog, get_product, send_contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", get_catalog),
    path(f"{CatalogConfig.name}/<int:product_id>/", get_product),
    path("", send_contacts),
]
