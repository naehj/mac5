from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url('contact/new/',views.newcontact),
	url('success', views.successView),
]
