from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class HeaderFields(models.Model):
	"""docstring for HeaderFields"""
	logoimage = models.ImageField(verbose_name='Logo image *')
	headerURLoptions = ListCharField(
		base_field=models.CharField(max_length=60),
		size=4,
		max_length=(4 * 61),
		verbose_name='Header URL options list *'
	)
	headeroptions = ListCharField(
		#each item is a option in the header of the system
        base_field=models.CharField(max_length=60),
        size=4,
        max_length=(4 * 61), # 3 * 60 character nominals, plus commas
        verbose_name='Header options list *'
    )
