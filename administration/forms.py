from django import forms
from .models import Client
from django.db import models
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class ClientForms(forms.ModelForm):
	SERVICES_CHOICES = [('Serviços Contábeis (sem cobrança de décimo terceiro)','Serviços Contábeis (sem cobrança de décimo terceiro)'),
							('Conciliação Bancária (auditoria de vendas e recuperação crédito).','Conciliação Bancária (auditoria de vendas e recuperação crédito).'),
							('Automação Comercial (gestão corporativa da empresa).','Automação Comercial (gestão corporativa da empresa).'),
							('Soluções empresariais de Telefonia fixa, móvel e dados.','Soluções empresariais de Telefonia fixa, móvel e dados.'),
							('Seguros Patrimoniais, Empresariais e Pessoais.','Seguros Patrimoniais, Empresariais e Pessoais.'),
							('Soluções em Meios de Pagamento (máquina cartões de crédito e débito).','Soluções em Meios de Pagamento (máquina cartões de crédito e débito).')]
	serviços_que_você_deseja_escolher = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=SERVICES_CHOICES,)
	class Meta:
		model = Client
		fields = ('client_id','title', 'name', 'city', 'phonenumber')
		widgets = {
			'title': forms.Select(attrs={'class': 'form-control',
										'placeholder': 'Título'}),
			'name': forms.TextInput(attrs={'class': 'form-control',
										'placeholder': 'Nome',
										'name':'FNAME'}),
			#'surname': forms.TextInput(attrs={'class': 'form-control',
			#							'placeholder': 'Sobrenome',
			#							'name':'LNAME'}),
			'city': forms.TextInput(attrs={'class': 'form-control',
										'placeholder': 'Cidade'}),
			#'neighbourhood': forms.TextInput(attrs={'class': 'form-control',
			#							'placeholder': 'CEP'}),
			#'yearofbirth': forms.Select(attrs={'class': 'form-control',
			#							'placeholder': 'Year of Birth',
			#							'type':'number'}),
			#'monthrofbirth': forms.Select(attrs={'class': 'form-control',
			#							'placeholder': 'Month of Birth',
			#							'type':'number'}),
			#'dayofbirth': forms.Select(attrs={'class': 'form-control',
			#							'placeholder': 'Day of Birth',
			#							'type':'number'})
			'bday': forms.DateTimeInput(attrs={'class': 'form-control',
												  'type':'date'}),
			'phonenumber': forms.TextInput(attrs={'class': 'form-control',
												  'type' : 'tel',
												  'placeholder': '(XX) X XXXX-XXXX',
												  'name':'PHONE'})
			}
