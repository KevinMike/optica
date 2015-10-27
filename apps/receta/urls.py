from django.conf.urls import patterns,  url, include
from .views import Index,EditarView


urlpatterns = patterns('',
   url(r'^$',Index.as_view(),name="index"),
   url(r'^editar/(\d+)/$',EditarView.as_view(),name="editar"),
)