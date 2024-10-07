import uuid
from django.db import models
from django_quill.fields import QuillField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254, verbose_name=_('Nome'))
    description = QuillField(verbose_name=_('Descrição'))
