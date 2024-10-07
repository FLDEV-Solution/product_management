from django.urls import path
from . import views


urlpatterns = [
    path("product", views.create, name="product_create")
]
