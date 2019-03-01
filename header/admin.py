from django.contrib import admin
from .models import HeaderFields

# Register your models here.
class HeaderFieldsAdmin(admin.ModelAdmin):
	list_display = ['logoimage', 'headeroptions']

admin.site.register(HeaderFields,HeaderFieldsAdmin)