from django.conf.urls import patterns,  url, include
from .views import *
from optica import settings

urlpatterns = patterns('',

    url(r'^$', Index.as_view(),name='index'),

)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))