from django import forms
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")

tasks = ["Learn Django", "IBM skills guide", "BCG X Data science cource"]
def index (request):
    return  render(request, "tasks/index.html", {
        "tasks":tasks
    })

def add (request):
    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
     })