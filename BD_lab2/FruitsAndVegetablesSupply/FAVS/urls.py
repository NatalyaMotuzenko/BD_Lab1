from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^$', views.index, name='index'), #default homepage
    url(r'^query/', views.query, name='query'),
]
