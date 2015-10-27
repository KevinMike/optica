from django.conf.urls import patterns,  url, include
from .views import *

urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^reporte/(\d+)/$','apps.facturacion.views.reporte',name='reporte'),
    url(r'^historial/$',HistorialView.as_view(),name="historial"),
    url(r'^notas/$',NotaPedidoView.as_view(),name="nota"),
    url(r'^nota_pedido/(\d+)/$',NotaPedidoPayment.as_view(),name='cancelar_nota_pedido'),
    #url(r'^login$','',name='reporte'),
    #url(r'^estadisticas$','apps.facturacion.views.estadisticas',name='estadisticas'),
)