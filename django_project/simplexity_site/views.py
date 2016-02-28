from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hi Kory & Marketa! My name is Simplexity, and I am online.")
