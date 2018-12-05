from django.urls import path
from .views import *


urlpatterns = [
    path('agregar', CrearTiendas.as_view(), name='crear_tiendas'),
]
