from django.shortcuts import render
from .models import HeaderFields

# Create your views here.
def header(request):
	header = HeaderFields.objects.all()
	return render(request, 'header/header.html', {'header':header})