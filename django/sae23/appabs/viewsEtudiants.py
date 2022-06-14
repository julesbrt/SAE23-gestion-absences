from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import EtudiantsForm

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = EtudiantsForm(request)
        return render(request, "appabs/ajoutetu.html", {"form": form})
    else:
        form = EtudiantsForm()
        return render(request, "appabs/ajoutetu.html", {"form": form})

def affiche(request, id):
    etudiants = models.Etudiants.objects.get(pk=id)
    return render(request, "appabs/afficheetu.html", {"etudiants": etudiants})

def modif(request, id):
    etudiants = models.Etudiants.objects.get(pk=id)
    form = EtudiantsForm(etudiants.dico())
    return render(request, "appabs/ajoutetu.html", {"form": form, "id": id})

def supprimer(request, id):
    etudiants = models.Etudiants.objects.get(pk=id)
    etudiants.delete()
    return HttpResponseRedirect("/appabs/main/")

def sauvegarder(request, id):
    eform = EtudiantsForm(request.POST)
    if eform.is_valid():
        enseignants = eform.save(commit=False)
        enseignants.id = id
        enseignants.save()
        return HttpResponseRedirect("/appabs/main/")
    else:
        return render(request, "appabs/ajoutetu.html", {"form": eform, "id": id})