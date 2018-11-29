from django.urls import path
from .views import *


urlpatterns = [
    path('registrar', usuario_add, name="agregar_usuario")
]
