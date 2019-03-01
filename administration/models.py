from django.db import models

# Create your models here.
class Client(models.Model):
	"""docstring for Client"""
	client_id = models.AutoField(primary_key = True)
	TITLE_CHOICES = [('Mr','Mr'), ('Miss','Miss'), ('Mrs','Mrs'), ('Ms','Ms'), ('Dr','Dr')]
	title = models.CharField(max_length = 500, choices = TITLE_CHOICES, default = '1')
	name = models.CharField(max_length=500, verbose_name='Nome *')
	surname = models.CharField(max_length=500, verbose_name='Sobrenome *', blank = True, null = True)
	bday = models.DateField(verbose_name='Data de Nascimento *', blank = True, null = True)
	city = models.CharField(max_length=500, verbose_name='Cidade *', blank = True, null = True)
	neighbourhood = models.CharField(max_length=500, verbose_name='CEP *', blank = True, null = True)
	age = models.IntegerField()
	phonenumber = models.IntegerField(verbose_name='Telefone *')
	quotation = models.FileField(verbose_name='Cotação *', blank = True, null = True)
	services = models.ManyToManyField('servicespage.ModuleService',blank = True)
	
	def __str__(self):
		return '{}'.format(self.name)
	

	def get_services(self):
		return "\n".join([s.services for s in self.service.all()])