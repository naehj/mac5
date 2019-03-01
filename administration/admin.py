from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
	list_display = ['client_id','title', 'name', 'surname', 'bday','city','neighbourhood', 'phonenumber', 'quotation']

admin.site.register(Client,ClientAdmin)