from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListView.as_view(), name="catalog"),
    path(f"{CatalogConfig.name}/<int:pk>/", CatalogDetailView.as_view(), name="product"),
]
