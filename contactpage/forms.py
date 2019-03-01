from django import forms
from .models import Contact
from django.db import models

class ContactForms(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name', 'email', 'phonenumber', 'website', 'message')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control',
										'placeholder': 'Seu nome'}),
			'email': forms.TextInput(attrs={'class': 'form-control',
										'placeholder': 'Seu endereço de email'}),
			'phonenumber': forms.TextInput(attrs={'class': 'form-control phone',
												  'type' : 'tel',
												  'placeholder': 'Seu número de telefone (opcional)'}),
			'website': forms.TextInput(attrs={'class': 'form-control',
										'placeholder': 'Seu web site (opcional)'}),
			'message': forms.TextInput(attrs={'class': 'form-control',
										'placeholder': 'Digite sua mensagem aqui...',
										'rows':'3'})
		}