from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForms
from django.conf import settings
# Create your views here.
def newcontact(request):
	if request.method == "POST":
		form = ContactForms(request.POST)
		if form.is_valid():
			contact = form.save(commit=False)
			subject = form.cleaned_data['name']
			from_email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			messagetoemail = 'Cliente: ' + subject + '\n' + 'Mensagem: ' + message
			contact.save()
			try:
				send_mail('Mac 5 Website', messagetoemail, settings.EMAIL_HOST_USER,['jimmy@arbid.com.br'],fail_silently=False)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('/contactpage/success')
	else:
		form = ContactForms()
	

	return render(request,'contactpage/newcontact.html', {'form':form})

def successView(request):
	return HttpResponse('Success! Thank you for your message.')