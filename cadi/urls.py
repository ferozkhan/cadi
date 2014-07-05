from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^cadi/(?P<width>\d+)x(?P<height>\d+)/$', views.cadi, name='cadi'),
)
