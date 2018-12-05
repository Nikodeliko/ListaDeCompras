from django.shortcuts import render
from .models import Tiendas
from .forms import CrearTiendaForm,ActualizarTiendaForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
# Create your views here.

class ListarTiendas(ListView):
	context_object_name = 'tienda'
	model = Tiendas
	template_name = 'tienda/lista_tienda.html'

class ActualizarTiendas(UpdateView):
	form_class = ActualizarTiendaForm
	template_name = 'tienda/actualizar_tienda.html'
	model = Tiendas
	success_url='/tienda'

class CrearTiendas(CreateView):
	form_class = CrearTiendaForm
	template_name = 'tienda/crear_tienda.html'
	model = Tiendas
	success_url = '/tienda'

class EliminarTiendas(DeleteView):
	model = Tiendas
	success_url='/tienda'
	template_name = 'tienda/eliminar_tienda.html'
