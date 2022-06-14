from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import GroupeEtudiantForm

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = GroupeEtudiantForm(request)
        return render(request, "appabs/ajoutgrp.html", {"form": form})
    else:
        form = GroupeEtudiantForm()
        return render(request, "appabs/ajoutgrp.html", {"form": form})

def affiche(request, id):
    groupeetu = models.GroupeEtudiant.objects.get(pk=id)
    return render(request, "appabs/affichegrp.html", {"groupeetu": groupeetu})

def modif(request, id):
    groupeetu = models.GroupeEtudiant.objects.get(pk=id)
    form = GroupeEtudiantForm(groupeetu.dico())
    return render(request, "appabs/ajoutgrp.html", {"form": form, "id": id})

def supprimer(request, id):
    groupeetu = models.GroupeEtudiant.objects.get(pk=id)
    groupeetu.delete()
    return HttpResponseRedirect("/appabs")

def sauvegarder(request, id):
    gform = GroupeEtudiantForm(request.POST)
    if gform.is_valid():
        groupeetu = gform.save(commit=False)
        groupeetu.id = id
        groupeetu.save()
        return HttpResponseRedirect("/appabs")
    else:
        return render(request, "appabs/ajoutgrp.html", {"form": gform, "id": id})