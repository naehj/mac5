from django.contrib import admin
from .models import Service, ModuleService

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['service_id','nameoftheservice', 'image','category', 'URLtotheservice']

admin.site.register(Service,ServiceAdmin)

class ModuleServiceAdmin(admin.ModelAdmin):
	list_display = ['page_title', 'pathlist',
					'firstsectiontitleofservice','firstsectionfirstdescription', 'firstsectionseconddescription', 'firstsectiionlistimage', 'firstsectionimagescarousel', 'firstsectionworkslist',
					'secondsectiontitle', 'secondsetiontitlesofservicesincludes', 'secondsetiondescriptionssofservicesincludes',
					'thirdsectiontitle', 'thirdsectionkindsofservicestitles', 'thirdsectionkindsofservicesdescription',
					'fourthserctiontitle', 'fourthserctionpricingoptionstitles', 'fourthserctionfirstpricingoptionprice', 'fourthserctionfirstpricingoptionfeatures', 'fourthserctionsecondpricingoptionprice', 'fourthserctionsecondpricingoptionfeatures', 'fourthserctionthirdpricingoptionprice', 'fourthserctionthirdpricingoptionfeatures',
					'fifthsectiontitle', 'fifthsectionteammembersname', 'fifthsectionfirstteammemberfunctions', 'fifthsectionsecondteammemberfunctions', 'fifthsectionthirdteammemberfunctions', 'fifthsectionfourthteammemberfunctions',
					'sixthsectiontitle', 'sixthsectiondescription']

admin.site.register(ModuleService,ModuleServiceAdmin)