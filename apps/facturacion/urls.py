from django.conf.urls import patterns,  url, include
from .views import *


urlpatterns = patterns('',

    url(r'^', IndexView.as_view(),name='index'),
)