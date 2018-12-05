from django.db import models
from django.contrib.auth.models import User

from apps.usuario.models import Perfil
from apps.producto.models import Productos

#Clase Abstracta para ver fecha de modificacion y creacion
class TimeStampModel(models.Model):
    creada = models.DateField(auto_now_add=True)
    modificada = models.DateField(auto_now=True)
    class Meta:
        abstract = True

class ListaCompras(TimeStampModel):
    propietario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    total_productos=models.PositiveIntegerField(default=0)
    total_productos_comprados=models.PositiveIntegerField(default=0)
    costo_total_presupuestado = models.PositiveIntegerField(default=0)
    costo_total_real = models.PositiveIntegerField(default=0)
    productos = models.ManyToManyField(Productos)

    def __unicode__(self):
        return self.ID;
