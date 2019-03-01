from django.shortcuts import render
from .forms import ClientForms
from .models import Client
import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

# Create your views here.
def newclient(request):
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
	

	return render(request,'administration/newclient.html', {'form':form, 'message':message,'status':status})

def allclients(request):
	if request.user.is_authenticated:
		clients = Client.objects.all()
		return render(request, 'administration/allclients.html', {'clients': clients,
            })
	else:
		return HttpResponse("hello you are not logged in")