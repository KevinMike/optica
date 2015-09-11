from django.conf.urls import patterns,  url, include
from .views import *


urlpatterns = patterns('',

    url(r'^buscar-cliente/(\d+)$','apps.cliente.views.SearchClient',),
    url(r'^guardar-cliente/$','apps.cliente.views.SaveClient',name="GuardarCliente"),
)