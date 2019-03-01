from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class HomeFields(models.Model):
	"""docstring for HomeFields"""
	#First Section#
	#initial title
	uppertitle = ListCharField(
		#the first item is to be the first line of the title and the second is the second line
        base_field=models.CharField(max_length=80),
        size=2,
        max_length=(2 * 81), # 2 * 60 character nominals, plus commas
        verbose_name='Upper title list *'
    )
	initialdescription = models.TextField(verbose_name='Initial description field *')
	#end First Section#
	
	#Second Section#
	tabs = ListCharField(
		#each item is a tab in the system
        base_field=models.CharField(max_length=60),
        size=3,
        max_length=(3 * 61), # 3 * 60 character nominals, plus commas
        verbose_name='Tab title list *'
    )
	#first tab data#
	firsttabsubtitle = models.TextField(verbose_name='First tab first subtitle *')
	firsttabsecondsubtitle = models.TextField(verbose_name='Firs tab second subtitle *')
	firsttabdescriprion = models.TextField(verbose_name='First tab description *')
	firsttabimage = models.ImageField(verbose_name='First tab image')
	firsttabvideoURL = models.URLField(verbose_name='First tab video URL *')
	#end first tab data#
	
	#second tab data#
	secondtabsubtitle = models.TextField(verbose_name='Second tab subtitle *')
	secondtabdescription = models.TextField(verbose_name='Second tab description *')
	#end second tab data#

	#third tab data#
	thirdtabsubtitle = models.TextField(verbose_name='Third tab subtitle *')
	thirdtabdescription = models.TextField(verbose_name='Third tab description *')
	thirdtablist = ListCharField(
		#each item is a description in the third tab
        base_field=models.CharField(max_length=60),
        size=4,
        max_length=(4 * 61), # 4 * 60 character nominals, plus commas
        verbose_name='Tab title list *'
    )
	#end third tab data#
	#end Second Section#
	
	#Third Section#

	#end Third Section#