from django.shortcuts import render
from .models import WhoWeAreFields

# Create your views here.
def whoweare(request):
	quemsomos = WhoWeAreFields.objects.get(page_title='Quem Somos?')
	return render(request, 'whoweare/whoweare.html', {'quemsomos':quemsomos})