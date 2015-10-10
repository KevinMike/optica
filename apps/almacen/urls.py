from django.conf.urls import patterns,  url, include
from .views import *
from optica import settings

urlpatterns = patterns('',

    url(r'^productos$', Productos.as_view(),name='producto'),
    url(r'^obtener-producto', 'apps.almacen.views.ObtenerProducto',name='ObtenerProducto'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))