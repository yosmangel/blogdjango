from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_home(request):
	if request.user.is_authenticated:
		context={
			"titulo": "hola persona especial"
		}
	else:
		context={
			"titulo": "List"
		}	
	return render(request, "index.html",context)

def post_create(request):
	return HttpResponse("<h1> Hola mundo create</h1>")

def post_detail(request):
	return HttpResponse("<h1> Hola mundodetail </h1>")

def post_update(request):
	return HttpResponse("<h1> Hola mundo update</h1>")

def post_delete(request):
	return HttpResponse("<h1> Hola mundo delete</h1>")