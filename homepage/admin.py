from django.contrib import admin
from .models import HomeFields

# Register your models here.
class HomeFieldsAdmin(admin.ModelAdmin):
	list_display = ['uppertitle', 'initialdescription', 'tabs','firsttabsubtitle']

admin.site.register(HomeFields,HomeFieldsAdmin)

		