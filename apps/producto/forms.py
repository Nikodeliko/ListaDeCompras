from django import forms
from .model import Productos

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'nombre',
            'costo_presu',
            'costo_real',
            'notas',
        ]

        label= {
            'nombre': 'Nombre del producto',
            'costo_presu': 'Costo Estimado',
            'costo_real': 'Costo Real',
            'notas': 'comentario adicional',
        }
