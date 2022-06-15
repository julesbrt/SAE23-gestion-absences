from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import AbsencesForm
from .models import Absences

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = AbsencesForm(request)
        return render(request, "appabs/ajoutabs.html", {"form": form})
    else:
        form = AbsencesForm()
        return render(request, "appabs/ajoutabs.html", {"form": form})

def affiche(request, id):
    absences = models.Absences.objects.get(pk=id)
    return render(request, "appabs/afficheabs.html", {"absences": absences})

def modif(request, id):
    absences = models.Absences.objects.get(pk=id)
    form = AbsencesForm(absences.dico())
    return render(request, "appabs/ajoutabs.html", {"form": form, "id": id})

def supprimer(request, id):
    absences = models.Absences.objects.get(pk=id)
    absences.delete()
    return HttpResponseRedirect("/appabs/main/")

def sauvegarder(request):
    aform = AbsencesForm(request.POST)
    if aform.is_valid():
        absences = aform.save()
        return HttpResponseRedirect("/appabs/main/")
    else:
        return render(request, "appabs/ajoutabs.html", {"form": aform})

def updatesauvegarder(request, id):
    aform = AbsencesForm(request.POST)
    if aform.is_valid():
        absences = aform.save(commit=False)
        absences.id = id
        absences.save()
        return HttpResponseRedirect("/appabs/main/")
    else:
        return render(request, "appabs/ajoutabs.html", {"form": aform, "id": id})