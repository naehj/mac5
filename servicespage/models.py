from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class Service(models.Model):
	"""docstring for HomeFields"""
	service_id = models.AutoField(primary_key = True)
	nameoftheservice = models.CharField(max_length = 500, verbose_name = 'Name of the Service *', blank=True, null=True)
	image = models.ImageField(verbose_name = 'Image of the service *', blank=True, null=True)
	CATEGORY_CHOICES = [('Serviços de Contabilidade', 'Serviços de Contabilidade'), ('Conciliação Bancária', 'Conciliação Bancária'), ('Meios de Pagamento','Meios de Pagamento'), ('Automação Comercial','Automação Comercial'), ('Seguros','Seguros'), ('Telefonia','Telefonia')]
	category = models.CharField(max_length = 500, verbose_name = 'Category of the service *', choices = CATEGORY_CHOICES, blank=True, null=True)
	URLtotheservice = models.CharField(max_length=500, verbose_name = 'URL to the service *', blank=True, null=True)
	module_service = models.ForeignKey('ModuleService', on_delete='CASCADE', blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.nameoftheservice)

class ModuleService(models.Model):
	"""docstring for ModuleService"""
	module_service_id = models.AutoField(primary_key = True)

	#Generic Data of the page#
	page_title = models.TextField(verbose_name = 'Title of the page *')
	pathlist = ListCharField(
        base_field=models.CharField(max_length=60),
        size=6,
        max_length=(6 * 61), # 6 * 10 character nominals, plus commas
        verbose_name='Path list *'
    )
    #end Generic Data of the page#

    #First section#
	firstsectiontitleofservice = models.TextField(verbose_name = 'Title of the service *', blank=True, null=True)
	firstsectionfirstdescription = models.TextField(verbose_name = 'First description of the service *', blank=True, null=True)
	firstsectionseconddescription = models.TextField(verbose_name = 'Second description of the service *', blank=True, null=True)
	firstsectiionlistimage = models.ImageField(verbose_name = 'First section image *', blank=True, null=True)
	firstsectionworkslist = ListCharField(
        base_field=models.CharField(max_length=500),
        size=20,
        max_length=(20 * 501),  # 6 * 10 character nominals, plus commas
        verbose_name='Works list *',
        blank=True,
		null=True
    )
	firstsectionimagescarousel = ListCharField(
		base_field=models.CharField(max_length=60),
		size=3,
		max_length=(3 * 61),
		verbose_name='Path to the images *',
		blank=True,
		null=True
	)
	#end First Section#
	
	#Second section#
	secondsectiontitle = models.TextField(verbose_name = 'Title of the includes of the services *', blank=True, null=True)
	secondsetiontitlesofservicesincludes = ListCharField(
		base_field=models.CharField(max_length=60),
		size=31,
		max_length=(31 * 66),
		verbose_name = 'Titles of services includes *',
		blank=True,
		null=True
	)
	secondsetiondescriptionssofservicesincludes = ListCharField(
		base_field=models.CharField(max_length=500),
		size=31,
		max_length=(31 * 506),
		verbose_name = 'Descriptions of services includes *',
		blank=True,
		null=True
	)
	#end Second Section#
	
	#Third Section#
	thirdsectiontitle = models.TextField(verbose_name = 'Title of the how can we help you section *', blank=True, null=True)
	thirdsectionkindsofservicestitles = ListCharField(
		base_field=models.CharField(max_length=500),
		size=7,
		max_length=(7 * 501),
		verbose_name = 'Titles of kinds of services *',
		blank=True,
		null=True
	)
	thirdsectionkindsofservicesdescription = ListCharField(
		base_field=models.CharField(max_length=2000),
		size=7,
		max_length=(7 * 2001),
		verbose_name = 'Descriptions of kinds of services *',
		blank=True,
		null=True
	)
	#end Third Section#

	#Fourth Section#
	fourthserctiontitle = models.TextField(verbose_name = 'Title o the pricing options *', blank=True, null=True)
	fourthserctionpricingoptionstitles =  ListCharField(
		base_field=models.CharField(max_length=60),
		size=6,
		max_length=(6 * 61),
		verbose_name = 'Titles of pricing options *',
		blank=True,
		null=True
	)
	fourthserctionfirstpricingoptionprice =  ListCharField(
		base_field=models.CharField(max_length=20),
		size=3,
		max_length=(3 * 21),
		verbose_name = 'Price of the first pricing option *',
		blank=True,
		null=True
	)
	fourthserctionfirstpricingoptionfeatures =  ListCharField(
		base_field=models.CharField(max_length=80),
		size=5,
		max_length=(5 * 81),
		verbose_name = 'Features of the first pricing option *',
		blank=True,
		null=True
	)
	fourthserctionsecondpricingoptionprice =  ListCharField(
		base_field=models.CharField(max_length=20),
		size=3,
		max_length=(3 * 21),
		verbose_name = 'Price of the second pricing option *',
		blank=True,
		null=True
	)
	fourthserctionsecondpricingoptionfeatures =  ListCharField(
		base_field=models.CharField(max_length=80),
		size=5,
		max_length=(5 * 81),
		verbose_name = 'Features of the second pricing option *',
		blank=True,
		null=True
	)
	fourthserctionthirdpricingoptionprice =  ListCharField(
		base_field=models.CharField(max_length=20),
		size=3,
		max_length=(3 * 21),
		verbose_name = 'Price of the third pricing option *',
		blank=True,
		null=True
	)
	fourthserctionthirdpricingoptionfeatures =  ListCharField(
		base_field=models.CharField(max_length=80),
		size=5,
		max_length=(5 * 81),
		verbose_name = 'Features of the third pricing option *',
		blank=True,
		null=True
	)
	#end Fourth Section#
	
	#Fifth Section#
	fifthsectiontitle = models.TextField(verbose_name='Global Team Title *', blank=True, null=True)
	fifthsectionteammembersname = ListCharField(
		base_field=models.CharField(max_length=80),
		size=4,
		max_length=(4 * 81),
		verbose_name = 'Names of the members of the global team *',
		blank=True,
		null=True
	)
	fifthsectionfirstteammemberfunctions = ListCharField(
		base_field=models.CharField(max_length=80),
		size=4,
		max_length=(4 * 81),
		verbose_name = 'First team member functions *',
		blank=True,
		null=True
	)
	fifthsectionsecondteammemberfunctions = ListCharField(
		base_field=models.CharField(max_length=80),
		size=4,
		max_length=(4 * 81),
		verbose_name = 'Second team member functions *',
		blank=True,
		null=True
	)
	fifthsectionthirdteammemberfunctions = ListCharField(
		base_field=models.CharField(max_length=80),
		size=4,
		max_length=(4 * 81),
		verbose_name = 'Third team member functions *',
		blank=True,
		null=True
	)
	fifthsectionfourthteammemberfunctions = ListCharField(
		base_field=models.CharField(max_length=80),
		size=4,
		max_length=(4 * 81),
		verbose_name = 'Fourth team member functions *',
		blank=True,
		null=True
	)
	#end Fifth Section#
	
	#Sixth Section#
	sixthsectiontitle = models.TextField(verbose_name='First-class business service title *', blank=True, null=True)
	sixthsectiondescription = models.TextField(verbose_name='First-class business service description *', blank=True, null=True)
	#end Sixth Section#

	def __str__(self):
		return '{}'.format(self.page_title)