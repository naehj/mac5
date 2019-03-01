from django.contrib import admin
from .models import WhoWeAreFields

# Register your models here.
class WhoWeAreAdmin(admin.ModelAdmin):
	list_display = ['page_title', 'pathlist',
					'firstsectionabouttitles','firstsectionaboutURLS',
					'secondsectioncompanyoverviewtitle', 'secondsectioncompanyoverviewdescription',
					'thirdsectionenterprisetitle', 'thirdsectionenterprisedescription',
					'fourthsectionmissionvisionvaluestitles', 'fourthsectionmissionvisionvaluesdescriptions', 'fourthsectionmissionvisionvaluesdescriptionsinlist']

admin.site.register(WhoWeAreFields,WhoWeAreAdmin)