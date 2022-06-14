from django.shortcuts import render
from . import models


# Create your views here.

def accueil(request):
    return render(request, "appabs/accueil.html")