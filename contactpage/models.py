from django.db import models

# Create your models here.
class Contact(models.Model):
	"""docstring for ContactFields"""
	contact_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 500, verbose_name = 'Your Name *')
	email = models.EmailField(verbose_name = 'Your Email Address *')
	phonenumber = models.PositiveIntegerField(blank = True,null=True, verbose_name = 'Your Phone Number (optional)')
	website = models.URLField(blank= True, null=True, verbose_name = 'Your Web Site (optional)')
	message = models.TextField(verbose_name = 'Your Message *')

	def __str__(self):
		return '{}'.format(self.name)