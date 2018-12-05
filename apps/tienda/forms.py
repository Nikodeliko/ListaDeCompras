from django import forms
from .models import Tiendas


class CrearTiendaForm(forms.ModelForm):
		class Meta:
			model = Tiendas
            exclude = ['estado']
			widgets = {
				'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'sucursal': forms.TextInput(attrs={'class': 'form-control'}),
				'direccion': forms.TextInput(attrs={'class': 'form-control'}),
				'sitio_web': forms.TextInput(attrs={'class': 'form-control'}),
			}

class ActualizarTiendaForm(forms.ModelForm):
		class Meta:
			model = Tiendas
			widgets = {
				'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'sucursal': forms.TextInput(attrs={'class': 'form-control'}),
				'direccion': forms.TextInput(attrs={'class': 'form-control'}),
				'sitio_web': forms.TextInput(attrs={'class': 'form-control'}),
                'estado': forms.Select(attrs={'class': 'form-control'}),
			}
