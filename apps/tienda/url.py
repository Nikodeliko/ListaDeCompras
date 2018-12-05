from django.conf.urls import patterns, url
from .views import ListarTiendas, ActualizarTiendas, CrearTiendas, EliminarTiendas

#Tienda
urlpatterns = patterns('',
	url(r'^tienda/$', ListarTiendas.as_view(), name = 'lista_productos'),
	url(r'^tienda/actualizar/(?P<pk>\d+)/$', ActualizarTiendas.as_view(), name ="actualizar_productos"),
	url(r'^tienda/agregar$', CrearTiendas.as_view(), name='crear_productos'),
	url(r'^tienda/eliminar/(?P<pk>\d+)/$', EliminarTiendas.as_view(), name="eliminar_productos"),
    )
