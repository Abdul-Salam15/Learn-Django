from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("salam/", views.salam, name = "salam"),
    path("malik/", views.malik, name = "malik"),
    # greet function url pattern
    path("<str:name>", views.greet, name = "greet")

]