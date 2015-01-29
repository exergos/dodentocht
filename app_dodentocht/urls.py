__author__ = 'Willem Lenaerts'

from django.conf.urls import patterns, url
from app_dodentocht import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^your-name/$', views.results, name='results'),
        url(r'^your-name/compare/$', views.compare, name='compare'),
        )