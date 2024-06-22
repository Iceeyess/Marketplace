from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView, ContactView, BlogCreateView, BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogListView.as_view(), name="catalog"),
    path(f"{CatalogConfig.name}/<int:pk>/", CatalogDetailView.as_view(), name="product"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("view/", BlogListView.as_view(), name="blog_view"),
    path("detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("update/<int:pk>/", BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete"),

]
