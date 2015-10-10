from django.conf.urls import patterns,  url, include
from .views import *

urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^reporte/(\d+)/$','apps.facturacion.views.reporte',name='reporte'),
    #url(r'^login$','',name='reporte'),
    #url(r'^estadisticas$','apps.facturacion.views.estadisticas',name='estadisticas'),
)