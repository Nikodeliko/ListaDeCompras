from django.urls import path
from apps.producto.views import *


urlpatterns = [
    path('agregar', CrearProductos.as_view(), name='crear_productos'),
	path('eliminar/(?P<pk>\d+)/$', EliminarProductos.as_view(), name="eliminar_productos"),
]
