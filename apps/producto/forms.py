from django import forms
from apps.producto.models import Productos

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Productos

		widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'costo_pre': forms.NumberInput(attrs={'class': 'form-control'}),
			'costo_real': forms.NumberInput(attrs={'class': 'form-control'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
			'tienda': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
		}
