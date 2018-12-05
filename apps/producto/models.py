from django.db import models
from apps.tienda.models import Tiendas

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(unique=True, null=False,max_length=40)
    costo_pre = models.IntegerField()
    costo_real = models.IntegerField()
    notas = models.CharField(max_length=300)
    tienda = models.ManyToManyField(Tiendas)

    def __str__(self):
        return '{}'.format(self.nombre)
