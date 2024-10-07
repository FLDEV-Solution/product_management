from django import forms
from django.utils.translation import gettext, gettext_lazy as _, pgettext
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description"]
