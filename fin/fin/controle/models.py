from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class gastos(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField(auto_now_add=False)
    observacao = models.TextField()


