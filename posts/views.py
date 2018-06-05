from django.shortcuts import render
from django.htpp import HttpRespose
# Create your views here.

def post_home(request):
	return HttpResponse("<h1> Hola mundo</h1>")