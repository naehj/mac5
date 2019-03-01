from django.shortcuts import render
from .models import HomeFields

# Create your views here.
def home(request):
	return render(request, 'homepage/home.html')