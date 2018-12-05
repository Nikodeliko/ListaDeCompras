from django.conf.urls import url
from apps.usuario.views import *
urlpatterns = [
    url(r'^registrar$', usuario_add, name='agregar_usuario'),
]
