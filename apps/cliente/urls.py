from django.conf.urls import patterns,  url, include
from .views import Index


urlpatterns = patterns('',
    url(r'^$',Index.as_view(),name="index"),
    url(r'^buscar-cliente/(\d+)$','apps.cliente.views.SearchClient',),
    url(r'^guardar-cliente/$','apps.cliente.views.SaveClient',name="GuardarCliente"),

)
