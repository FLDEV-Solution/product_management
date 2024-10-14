from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .forms import ProductForm
from .models import Product


@login_required
def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request=request, template_name="form.html", context={'form': form, 'action': 'create'})


@login_required
def read(request, uuid=None):
    product = get_object_or_404(Product, uuid=uuid)
    return render(
        request=request, 
        template_name="read.html",
        context={
            'product': product, 'uuid': uuid
        }
    )


@login_required
def update(request, uuid=None):
    product = get_object_or_404(Product, uuid=uuid)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request=request, template_name="form.html", context={
        'form': form, 'product': product, 'action': 'update', 'uuid': uuid
    })


@login_required
@require_POST
@csrf_protect
def delete(request, uuid=None):
    if request.method == 'POST':
        product = get_object_or_404(Product, uuid=uuid)
        product.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Product deleted successfully.'
        })
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)
