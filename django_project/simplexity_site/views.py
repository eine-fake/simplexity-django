from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Simplexity on Django. Wilkommen.")

def files(request):
	return HttpResponse("<h1>Files</h1>")