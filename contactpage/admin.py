from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	list_display = ['contact_id','name', 'email', 'phonenumber', 'website']

admin.site.register(Contact,ContactAdmin)