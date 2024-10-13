from django.urls import path
from . import views


urlpatterns = [
    # path("products", views.create, name="products"),
    path("product/create", views.create, name="product_create"),
    path("product/<uuid:uuid>", views.read, name="product_read"),
    path("product/<uuid:uuid>/update", views.update, name="product_update"),
    path("product/<uuid:uuid>/delete", views.delete, name="product_delete"),
]
