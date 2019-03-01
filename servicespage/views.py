from django.shortcuts import render
from .forms import ServiceForms
from .models import Service, ModuleService
from administration.forms import ClientForms 
import datetime
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

# Create your views here.
def allservices(request):
	services = Service.objects.all()
	message = ''
	status = ''
	if request.method == "POST":
		form = ClientForms(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			diff = datetime.date.today() - client.bday
			if diff.days >= 0:
				client.age = diff.days//365
				message = 'Your request for a quotation has been sent'
				status = 'success'
				messagetoemail = 'Título: ' + client.title + '\n' + 'Nome: ' + client.name + '\n' + 'Cidade: ' + client.city + '\n' + 'Telefone: ' + str(client.phonenumber)
				try:
					send_mail('Mac 5 Website', messagetoemail, settings.EMAIL_HOST_USER,['jimmy@arbid.com.br'],fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				client.save()
				form = ClientForms()
			else:
				message = 'The data that you insert is invalid because is after today'
				status = 'danger'
			
	else:
		form = ClientForms()
		message = ''
		status = ''
	return render(request, 'servicespage/allservices.html', {'services':services, 'form':form, 'message':message, 'status':status})

def contabilityservices(request):
	service = ModuleService.objects.get(firstsectiontitleofservice__contains='Contabilidade')
	message = ''
	status = ''
	if request.method == "POST":
		form = ClientForms(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			diff = datetime.date.today() - client.bday
			if diff.days >= 0:
				client.age = diff.days//365
				message = 'Your request for a quotation has been sent'
				status = 'success'
				messagetoemail = 'Título: ' + client.title + '\n' + 'Nome: ' + client.name + '\n' + 'Cidade: ' + client.city + '\n' + 'Telefone: ' + str(client.phonenumber) + '\n' + 'Serviços'
				if client.serviços_que_você_deseja_escolher:
					for servico in serviços_que_você_deseja_escolher:
						messagetoemail += serviços_que_você_deseja_escolher
				try:
					send_mail('Mac 5 Website', messagetoemail, settings.EMAIL_HOST_USER,['jheanmarllos1@gmail.com'],fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				client.save()
				form = ClientForms()
			else:
				message = 'The data that you insert is invalid because is after today'
				status = 'danger'
	else:
		form = ClientForms()
		message = ''
		status = ''
	return render(request, 'servicespage/moduleservice.html', {'service':service,'form':form, 'message':message, 'status':status})

def bankreconciliation(request):
	service = ModuleService.objects.get(firstsectiontitleofservice__contains='Bancária')
	message = ''
	status = ''
	if request.method == "POST":
		form = ClientForms(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			diff = datetime.date.today() - client.bday
			if diff.days >= 0:
				client.age = diff.days//365
				message = 'Your request for a quotation has been sent'
				status = 'success'
				messagetoemail = 'Título: ' + client.title + '\n' + 'Nome: ' + client.name + '\n' + 'Sobrenome: ' + client.surname + '\n' + 'Data de nascimento: ' + str(client.bday) + '\n' + 'Cidade: ' + client.city + '\n' + 'CEP: ' + client.neighbourhood + '\n' + 'Idade: ' + str(client.age) + '\n' + 'Telefone: ' + str(client.phonenumber)
				try:
					send_mail('Mac 5 Website', messagetoemail, settings.EMAIL_HOST_USER,['jheanmarllos1@gmail.com'],fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				client.save()
				form = ClientForms()
			else:
				message = 'The data that you insert is invalid because is after today'
				status = 'danger'
	else:
		form = ClientForms()
		message = ''
		status = ''
	return render(request, 'servicespage/moduleservice.html', {'service':service,'form':form, 'message':message, 'status':status})

def paymentoptions(request):
	service = ModuleService.objects.get(firstsectiontitleofservice__contains='Pagamento')
	message = ''
	status = ''
	if request.method == "POST":
		form = ClientForms(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			diff = datetime.date.today() - client.bday
			if diff.days >= 0:
				client.age = diff.days//365
				message = 'Your request for a quotation has been sent'
				status = 'success'
				messagetoemail = 'Título: ' + client.title + '\n' + 'Nome: ' + client.name + '\n' + 'Sobrenome: ' + client.surname + '\n' + 'Data de nascimento: ' + str(client.bday) + '\n' + 'Cidade: ' + client.city + '\n' + 'CEP: ' + client.neighbourhood + '\n' + 'Idade: ' + str(client.age) + '\n' + 'Telefone: ' + str(client.phonenumber)
				try:
					send_mail('Mac 5 Website', messagetoemail, settings.EMAIL_HOST_USER,['jheanmarllos1@gmail.com'],fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				client.save()
				form = ClientForms()
			else:
				message = 'The data that you insert is invalid because is after today'
				status = 'danger'
	else:
		form = ClientForms()
		message = ''
		status = ''
	return render(request, 'servicespage/moduleservice.html', {'service':service,'form':form, 'message':message, 'status':status})

def commercialautomation(request):
	service = ModuleService.objects.get(firstsectiontitleofservice__contains='Automação')
	message = ''
	status = ''
	if request.method == "POST":
		form = ClientForms(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			diff = datetime.date.today() - client.bday
			if diff.days >= 0:
				client.age = diff.days//365
				message = 'Your request for a quotation has been sent'
				status = 'success'
				messagetoemail = 'Título: ' + client.title + '\n' + 'Nome: ' + client.name + '\n' + 'Sobrenome: ' + client.surname + '\n' + 'Data de nascimento: ' + str(client.bday) + '\n' + 'Cidade: ' + client.city + '\n' + 'CEP: ' + client.neighbourhood + '\n' + 'Idade: ' + str(client.age) + '\n' + 'Telefone: ' + str(client.phonenumber)
				try:
					send_mail('Mac 5 Website', messagetoemail, settings.EMAIL_HOST_USER,['jheanmarllos1@gmail.com'],fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				client.save()
				form = ClientForms()
			else:
				message = 'The data that you insert is invalid because is after today'
				status = 'danger'
	else:
		form = ClientForms()
		message = ''
		status = ''
	return render(request, 'servicespage/moduleservice.html', {'service':service,'form':form, 'message':message, 'status':status})

def insurance(request):
	service = ModuleService.objects.get(firstsectiontitleofservice__contains='Seguros')
	message = ''
	status = ''
	if request.method == "POST":
		form = ClientForms(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			diff = datetime.date.today() - client.bday
			if diff.days >= 0:
				client.age = diff.days//365
				message = 'Your request for a quotation has been sent'
				status = 'success'
				messagetoemail = 'Título: ' + client.title + '\n' + 'Nome: ' + client.name + '\n' + 'Sobrenome: ' + client.surname + '\n' + 'Data de nascimento: ' + str(client.bday) + '\n' + 'Cidade: ' + client.city + '\n' + 'CEP: ' + client.neighbourhood + '\n' + 'Idade: ' + str(client.age) + '\n' + 'Telefone: ' + str(client.phonenumber)
				try:
					send_mail('Mac 5 Website', messagetoemail, settings.EMAIL_HOST_USER,['jheanmarllos1@gmail.com'],fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				client.save()
				form = ClientForms()
			else:
				message = 'The data that you insert is invalid because is after today'
				status = 'danger'
	else:
		form = ClientForms()
		message = ''
		status = ''
	return render(request, 'servicespage/moduleservice.html', {'service':service,'form':form, 'message':message, 'status':status})

def telephonie(request):
	service = ModuleService.objects.get(firstsectiontitleofservice__contains='Telefonia')
	message = ''
	status = ''
	if request.method == "POST":
		form = ClientForms(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			diff = datetime.date.today() - client.bday
			if diff.days >= 0:
				client.age = diff.days//365
				message = 'Your request for a quotation has been sent'
				status = 'success'
				messagetoemail = 'Título: ' + client.title + '\n' + 'Nome: ' + client.name + '\n' + 'Sobrenome: ' + client.surname + '\n' + 'Data de nascimento: ' + str(client.bday) + '\n' + 'Cidade: ' + client.city + '\n' + 'CEP: ' + client.neighbourhood + '\n' + 'Idade: ' + str(client.age) + '\n' + 'Telefone: ' + str(client.phonenumber)
				try:
					send_mail('Mac 5 Website', messagetoemail, settings.EMAIL_HOST_USER,['jheanmarllos1@gmail.com'],fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				client.save()
				form = ClientForms()
			else:
				message = 'The data that you insert is invalid because is after today'
				status = 'danger'
	else:
		form = ClientForms()
		message = ''
		status = ''
	return render(request, 'servicespage/moduleservice.html', {'service':service,'form':form, 'message':message, 'status':status})

def newservice(request):
	if request.method == "POST":
		form = ServiceForms(request.POST)
		if form.is_valid():
			service = form.save(commit=False)
			service.save()
	else:
		form = ServiceForms()
	

	return render(request,'servicespage/newservice.html', {'form':form})