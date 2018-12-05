from django import forms
from .models import ListaCompras

class ListaForm(forms.ModelForm):
    class Meta:
        model = ListaCompras

        fields = [
            "propietario",
            "total_productos",
            "total_productos_comprados",
            "costo_total_presupuestado",
            "costo_total_real",
            "productos",
        ]
        widgets = {
            'propietario': forms.Select(attrs={'class': 'form-control'}),
			'total_productos': forms.NumberInput(attrs={'class': 'form-control'}),
			'total_productos_comprados': forms.NumberInput(attrs={'class': 'form-control'}),
            'costo_total_presupuestado': forms.NumberInput(attrs={'class': 'form-control'}),
            'costo_total_real': forms.NumberInput(attrs={'class': 'form-control'}),
			'productos': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
		}
