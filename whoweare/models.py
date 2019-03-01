from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class WhoWeAreFields(models.Model):
	"""docstring for WhoWeAreFields"""
	whoweare_id = models.AutoField(primary_key = True)

	#Generic Data of the page#
	page_title = models.TextField(verbose_name = 'Title of the page *')
	pathlist = ListCharField(
        base_field=models.CharField(max_length=60),
        size=6,
        max_length=(6 * 61), # 6 * 10 character nominals, plus commas
        verbose_name='Path list *'
    )
    #end of Generic Data of the page#
    
    #First Section#
	firstsectionabouttitles = ListCharField(
		base_field=models.CharField(max_length=60),
        size=7,
        max_length=(7 * 61), # 6 * 10 character nominals, plus commas
        verbose_name='First Section pages titles *',
        blank=True,
        null=True
	)
	firstsectionaboutURLS = ListCharField(
		base_field=models.CharField(max_length=60),
        size=7,
        max_length=(7 * 61), # 6 * 10 character nominals, plus commas
        verbose_name='First Section pages URLS *',
        blank=True,
        null=True
	)
	#end First Section#

	#Second Section#
	secondsectioncompanyoverviewtitle =  models.TextField(verbose_name = 'Second Section company overview title *', blank=True, null=True)
	secondsectioncompanyoverviewdescription =  models.TextField(verbose_name = 'Second Section company overview description *', blank=True, null=True)
	#end Second Section#

	#Third Section#
	thirdsectionenterprisetitle = models.TextField(verbose_name = 'Third Section enterprise title *', blank=True, null=True)
	thirdsectionenterprisedescription = models.TextField(verbose_name = 'Third Section enterprise description *', blank=True, null=True)
	#end Third Section#

	#Fourth Section#
	fourthsectionmissionvisionvaluestitles = ListCharField(
		base_field=models.CharField(max_length=60),
        size=3,
        max_length=(3 * 61), # 6 * 10 character nominals, plus commas
        verbose_name='Fourth Section mission vision and values titles *',
        blank=True,
        null=True
	)
	fourthsectionmissionvisionvaluesdescriptions = ListCharField(
		base_field=models.CharField(max_length=500),
        size=3,
        max_length=(3 * 501), # 6 * 10 character nominals, plus commas
        verbose_name='Fourth Section mission vision and values descriptions *',
        blank=True,
        null=True
	)
	fourthsectionmissionvisionvaluesdescriptionsinlist = ListCharField(
		base_field=models.CharField(max_length=500),
        size=5,
        max_length=(5 * 501), # 6 * 10 character nominals, plus commas
        verbose_name='Fourth Section mission vision and values descriptions in list *',
        blank=True,
        null=True
	)
	#end Fourth Section#