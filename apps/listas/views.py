from django.shortcuts import render
from django.urls import reverse_lazy
from .models import ListaCompras
from .forms import ListaForm
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
# Create your views here.

class CrearLista(CreateView):
	model = ListaCompras
	form_class = ListaForm
	template_name = 'listas/CrearLista.html'
	success_url = reverse_lazy('listas:crear_listas')

	def __init__(self, Perfil, *args, **kwargs):
		self.user = user
		super(RSVPForm, self).__init__(*args, **kwargs)

class ListasCompras(ListView):
    template_name = 'listas/ListarListas.html'
    model = ListaCompras

    def get_context_data(self, **kwargs):
        context = super(ListaCompras, self).get_context_data(**kwargs)
        context['events'] =Cabecera.objects.filter(propietario=self.request.user)
        context['compras'] = context['events']
        return context
