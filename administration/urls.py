from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url('client/new/', views.newclient),
	url('client/all/', views.allclients),
]
