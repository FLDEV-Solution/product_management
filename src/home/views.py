from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product


@login_required
def index(request):
    products = Product.objects.order_by("name")
    return render(request, "index.html", {'products': products})
