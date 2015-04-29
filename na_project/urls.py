from django.conf.urls import patterns, url
from na_project import views
from na_project.models import *

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)