from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import  CatalogDetailView, CatalogCreateView, CatalogDeleteView, CatalogUpdateView, \
    catalog_list

app_name = CatalogConfig.name

urlpatterns = [
    path("", catalog_list, name="product"),
    path(f"detail/<int:pk>/", CatalogDetailView.as_view(), name="product_detail"),
    path(f"create/", CatalogCreateView.as_view(), name="product_create"),
    path(f"edit/<int:pk>/", CatalogUpdateView.as_view(), name="product_update"),
    path(f"delete/<int:pk>/", CatalogDeleteView.as_view(), name="product_delete"),
]
