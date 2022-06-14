from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import EnseignantsForm

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = EnseignantsForm(request)
        return render(request, "appabs/ajoutens.html", {"form": form})
    else:
        form = EnseignantsForm()
        return render(request, "appabs/ajoutens.html", {"form": form})

def affiche(request, id):
    enseignants = models.Enseignants.objects.get(pk=id)
    return render(request, "appabs/afficheens.html", {"enseignants": enseignants})

def modif(request, id):
    enseignants = models.Enseignants.objects.get(pk=id)
    form = EnseignantsForm(enseignants.dico())
    return render(request, "appabs/ajoutens.html", {"form": form, "id": id})

def supprimer(request, id):
    enseignants = models.Enseignants.objects.get(pk=id)
    enseignants.delete()
    return HttpResponseRedirect("/appabs")

def sauvegarder(request, id):
    eform = EnseignantsForm(request.POST)
    if eform.is_valid():
        enseignants = eform.save(commit=False)
        enseignants.id = id
        enseignants.save()
        return HttpResponseRedirect("/appabs")
    else:
        return render(request, "appabs/ajoutens.html", {"form": eform, "id": id})