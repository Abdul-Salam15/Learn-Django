from django.urls import path
from . import views

#The app_name variable is built in and should not be changed, because Django specifically looks for the variable app_name
app_name = "taskee"
urlpatterns = [
    path("", views.index, name = "index"),
    path("add/", views.add, name = "add")
    ]