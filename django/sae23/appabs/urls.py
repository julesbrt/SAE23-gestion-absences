from django.urls import path
from . import views, viewsAbsences, viewsCours, viewsEtudiants, viewsGroupeEtudiants, viewsEnseignants

urlpatterns = [
    path('main/', views.main),

    path('absences/ajout', viewsAbsences.ajout),
    path('absences/affiche/', viewsAbsences.affiche),
    path('absences/modif/<int:id>/', viewsAbsences.modif),
    path('absences/supprimer/<int:id>/', viewsAbsences.supprimer),
    path('absences/updatesauvegarder/<int:id>/', viewsAbsences.updatesauvegarder),

    path('cours/ajout', viewsCours.ajout),
    path('cours/sauvegarder//', viewsCours.sauvegarder),
    path('cours/affiche/', viewsCours.affiche),
    path('cours/modifier/<int:id>/', viewsCours.modif),
    path('cours/supprimer/<int:id>/', viewsCours.supprimer),
    path('cours/updatesauvegarder/<int:id>/', viewsCours.updatesauvegarder),
    path('cours/updatesauvegarder//', viewsCours.sauvegarder),

    path('enseignants/ajout', viewsEnseignants.ajout),
    path('enseignants/sauvegarder//', viewsEnseignants.sauvegarder),
    path('enseignants/affiche/', viewsEnseignants.affiche),
    path('enseignants/modifier/<int:id>/', viewsEnseignants.modif),
    path('enseignants/supprimer/<int:id>/', viewsEnseignants.supprimer),
    path('enseignants/updatesauvegarder/<int:id>/', viewsEnseignants.updatesauvegarder),
    path('enseignants/updatesauvegarder//', viewsEnseignants.sauvegarder),

    path('etudiants/ajout', viewsEtudiants.ajout),
    path('etudiants/sauvegarder//', viewsEtudiants.sauvegarder),
    path('etudiants/affiche/', viewsEtudiants.affiche),
    path('etudiants/modifier/<int:id>/', viewsEtudiants.modif),
    path('etudiants/supprimer/<int:id>/', viewsEtudiants.supprimer),
    path('etudiants/updatesauvegarder/<int:id>/', viewsEtudiants.updatesauvegarder),
    path('etudiants/updatesauvegarder//', viewsEtudiants.sauvegarder),

    path('grpetudiants/ajout', viewsGroupeEtudiants.ajout),
    path('grpetudiants/sauvegarder//', viewsGroupeEtudiants.sauvegarder),
    path('grpetudiants/affiche/', viewsGroupeEtudiants.affiche),
    path('grpetudiants/modifier/<int:id>/', viewsGroupeEtudiants.modif),
    path('grpetudiants/supprimer/<int:id>/', viewsGroupeEtudiants.supprimer),
    path('grpetudiants/updatesauvegarder/<int:id>/', viewsGroupeEtudiants.updatesauvegarder),
    path('grpetudiants/updatesauvegarder//', viewsGroupeEtudiants.sauvegarder),

]
