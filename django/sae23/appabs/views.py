from django.shortcuts import render

# Create your views here.

def acceuil(request):
    return (request, "appabs/acceuil.html")