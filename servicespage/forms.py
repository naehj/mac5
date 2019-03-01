from django import forms
from .models import Service
from django.db import models

class ServiceForms(forms.ModelForm):
	class Meta:
		model = Service
		fields = ('nameoftheservice', 'image', 'category', 'URLtotheservice')
		widgets = {
			'nameoftheservice': forms.TextInput(attrs={'class': 'form-control',
										'placeholder': 'Service Name'}),
			'image': forms.FileInput(attrs={'class': 'form-control-file',
											'type' : 'file',
											'placeholder': 'Image for service'}),
			'category': forms.Select(attrs={'class': 'form-control'}),
			'URLtotheservice': forms.URLInput(attrs={'class': 'form-control',
										'placeholder': 'URL to the service'})
		}