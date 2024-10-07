from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request=request, template_name="create.html", context={'form': form})
