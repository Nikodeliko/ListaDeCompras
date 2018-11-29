from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]

        label= {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo',
            'username': 'Nombre de usuario',
            'password': 'Contraseña',
        }

        def save(self):
            password= self.cleaned_data.pop('password')
            u = super().save()
            u.set_password(password)
            u.save()
            return u
