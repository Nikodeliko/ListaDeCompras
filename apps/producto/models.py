from django.db import models
#from tienda.models impor Tiendas
# Create your models here.

class Producto(models.Model):
	Nombre = models.CharField(max_length=40)
	Costo_p = models.DecimalField(max_digits=5, decimal_places=2)
	Costo_real = models.DecimalField(max_digits=3, decimal_places=2)
	tienda = models.CharField(max_length=40)
	notas = models.CharField(max_length=200)