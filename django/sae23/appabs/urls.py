from django.urls import path
from . import views, viewsAbsences, viewsCours, viewsEtudiants, viewsGroupeEtudiants, viewsEnseignants

urlpatterns = [
    path('main/', views.main),

    path('absences/ajout', viewsAbsences.ajout),
    path('absences/sauvegarder//', viewsAbsences.sauvegarder),
    path('absences/affiche/', viewsAbsences.affiche),
    path('absences/modifier/<int:id>/', viewsAbsences.modif),
    path('absences/supprimer/<int:id>/', viewsAbsences.supprimer),
    path('absences/updatetraitement/<int:id>/', viewsAbsences.updatesauvegarder),
    path('absences/updatetraitement//', viewsAbsences.sauvegarder),

    path('cours/ajout', viewsCours.ajout),
    path('cours/affiche', viewsCours.affiche),
    path('cours/modifier', viewsCours.modif),
    path('cours/supprimer', viewsCours.supprimer),
    path('cours/sauvegarder', viewsCours.sauvegarder),

    path('enseignants/ajout', viewsEnseignants.ajout),
    path('enseignants/affiche', viewsEnseignants.affiche),
    path('enseignants/modifier', viewsEnseignants.modif),
    path('enseignants/supprimer', viewsEnseignants.supprimer),
    path('enseignants/sauvegarder', viewsEnseignants.sauvegarder),

    path('etudiants/ajout', viewsEtudiants.ajout),
    path('etudiants/affiche', viewsEtudiants.affiche),
    path('etudiants/modifier', viewsEtudiants.modif),
    path('etudiants/supprimer', viewsEtudiants.supprimer),
    path('etudiants/sauvegarder', viewsEtudiants.sauvegarder),

    path('grpetudiants/ajout', viewsGroupeEtudiants.ajout),
    path('grpetudiants/affiche', viewsGroupeEtudiants.affiche),
    path('grpetudiants/modifier', viewsGroupeEtudiants.modif),
    path('grpetudiants/supprimer', viewsGroupeEtudiants.supprimer),
    path('grpetudiants/sauvegarder', viewsGroupeEtudiants.sauvegarder)

]
