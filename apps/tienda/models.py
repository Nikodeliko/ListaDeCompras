from django.db import models

# Create your models here.

class Tiendas(models.Model):
	nombre = models.CharField(max_length=60, unique=True)
	sucursal = models.CharField(max_length=50, null=True)
	direccion = models.CharField(max_length=100, null=True)
	sitio_web = models.CharField(max_length=100, null=True)
	ESTADOS = (('P','Pendiente'),('A','Aceptado'))
	estado = models.CharField(max_length=1,choices=ESTADOS,null=False, default='P')

	def __str__(self):
		return '{}'.format(self.nombre)
