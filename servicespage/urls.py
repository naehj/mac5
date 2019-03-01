from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url('allservices/', views.allservices),
	url('servicosdecontabilidade/', views.contabilityservices),
	url('conciliacaobancaria/', views.bankreconciliation),
	url('opcoesdepagamento/', views.paymentoptions),
	url('automacaocomercial/', views.commercialautomation),
	url('seguros/', views.insurance),
	url('telefonia/', views.telephonie),
	url('newservice/', views.newservice)
]
