from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def salam(request):
    return HttpResponse("Hey Salam!!")
def malik(request):
    return HttpResponse("Hey Malik!!")

''' -> To create a view functio to say hello to anyone, we can use the below function
    -> .capitalize() gives the first letter a capital letter, it is quite differet from .upper() which makes the whole string an upper case'''
#def greet(request, name):
#    return HttpResponse(f"Hello {name.capitalize()}, you are welcome to this page!")

#To create a template so we have an html page
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })