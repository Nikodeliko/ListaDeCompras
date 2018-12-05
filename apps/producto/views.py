from django.shortcuts import render
from apps.producto.models import Productos
from apps.producto.views import ProductoForm
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
# Create your views here.

class ListaProductos(ListView):
	context_object_name = 'producto'
	model = Productos
	template_name = 'producto/lista_producto.html'

class ActualizarProductos(UpdateView):
	form_class = ProductoForm
	template_name = 'producto/actualizar_producto.html'
	model = Productos
	success_url='/producto'

class CrearProductos(CreateView):
	form_class = ProductoForm
	template_name = 'productos/crear_producto.html'
	model = Productos
	success_url = 'listas/CrearLista.html'

class EliminarProductos(DeleteView):
	model = Productos
	success_url='/producto'
	template_name = 'producto/eliminar_producto.html'
