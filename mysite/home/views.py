from django.shortcuts import render
from django.apps import apps

# Create your views here.

def home(request):
    #all_app = apps.get_models()
    #print(str(all_app))
    return render(request, "home/home.html")
