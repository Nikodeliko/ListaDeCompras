from django.urls import path
from apps.listas.views import *


urlpatterns = [
    path('agregar', CrearLista.as_view(), name="crear_listas")
]
