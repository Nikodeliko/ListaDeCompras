from django import forms
from .models import Tiendas


class CrearTiendaForm(forms.ModelForm):
	class Meta:
		model = Tiendas
		exclude = ['estado']
		fields = [
		    "nombre",
			"sucursal",
			"direccion",
			"sitio_web",
		]

		widgets = {
		    'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'sucursal': forms.TextInput(attrs={'class': 'form-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'sitio_web': forms.TextInput(attrs={'class': 'form-control'}),
		}
class ActualizarTiendaForm(forms.ModelForm):
	class Meta:
		model = Tiendas

		fields = [
		    "nombre",
			"sucursal",
			"direccion",
			"sitio_web",
			"estado",
		]

		widgets = {
		    'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'sucursal': forms.TextInput(attrs={'class': 'form-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'sitio_web': forms.TextInput(attrs={'class': 'form-control'}),
			'estado': forms.Select(attrs={'class': 'form-control'}),
		}
