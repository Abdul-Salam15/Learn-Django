from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasks = ["Learn Django", "IBM skills guide", "BCG X Data science cource"]
def index (request):
    return  render(request, "tasks/index.html", {
        "tasks":tasks
    })
