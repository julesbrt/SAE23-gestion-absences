from django.shortcuts import render, HttpResponseRedirect
from . import models
from .forms import CoursForm

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = CoursForm(request)
        return render(request, "appabs/ajoutcours.html", {"form": form})
    else:
        form = CoursForm()
        return render(request, "appabs/ajoutcours.html", {"form": form})

def affiche(request, id):
    cours = models.Cours.objects.get(pk=id)
    return render(request, "appabs/affichecours.html", {"cours": cours})

def modif(request, id):
    cours = models.Cours.objects.get(pk=id)
    form = CoursForm(cours.dico())
    return render(request, "appabs/ajoutcours.html", {"form": form, "id": id})

def supprimer(request, id):
    cours = models.Cours.objects.get(pk=id)
    cours.delete()
    return HttpResponseRedirect("/appabs")

def sauvegarder(request, id):
    cform = CoursForm(request.POST)
    if cform.is_valid():
        cours = cform.save(commit=False)
        cours.id = id
        cours.save()
        return HttpResponseRedirect("/appabs")
    else:
        return render(request, "appabs/ajoutcours.html", {"form": cform, "id": id})