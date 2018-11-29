from django.db import models
from django.contrib.auth.models import User

from usuario.models import Perfil
from producto.models import Productos

class ListaProductos(models.Model):
    producto = models.OneToOneField(Productos, on_delete=models.SET_NULL, null=True)

class ListaCompras(models.Model):
    propietario = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)
    listaproductos= models.ManyToManyField(ListaProductos)
