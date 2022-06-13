from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AbsencesForm(ModelForm):
    class Meta:
        model = models.Absences

        fields = ('idabsences', 'idetudiants', 'idcours', 'justificationcours', 'docjustcours')
        labels = {
            'idabsences': _('ID absence'),
            'idetudiants': _('ID etudiant'),
            'idcours': _('ID cours'),
            'justificationcours': _('Justification au cours'),
            'docjustcours': _('Document de justification'),
        }

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours

        fields = ('idcours', 'titrecours', 'datecours', 'idenseignants', 'dureecours','idgroupe')
        labels = {
            'idcours': _('ID cours'),
            'titrecours': _('Titre cours'),
            'datecours': _('Date cours'),
            'idenseignants': _('ID enseignants'),
            'dureecours': _('Durée cours'),
            'idgroupe': _('ID groupe'),
        }

class EnseignantsForm(ModelForm):
    class Meta:
        model = models.Enseignants

        fields = ('idetudiants', 'nometudiants', 'prenometudiant', 'emailetudiant', 'idgroupee','photoetudiant')
        labels = {
            'idetudiants': _('ID enseignants'),
            'nometudiants': _('Nom enseignats'),
            'prenometudiant': _('Prenom enseignants'),
            'emailetudiant': _('Email enseignants'),
            'idgroupee': _('ID groupe'),
            'photoetudiant': _('Photo étudiant'),
        }

class EtudiantsForm(ModelForm):
    class Meta:
        model = models.Etudiants

        fields = ('idetudiants', 'nometudiants','prenometudiant', 'emailetudiant','idgroupee','photoetudiant')
        labels = {
            'idetudiants': _('ID étudiants'),
            'nometudiants': _('Nom étudiants'),
            'prenometudiant': _('Prénom étudiant'),
            'emailetudiant': _('Email étudiant'),
            'idgroupee': _('ID groupe'),
            'photoetudiant': _('Photo étudiant'),
        }


class GroupeEtudiantForm(ModelForm):
    class Meta:
        model = models.GroupeEtudiant

        fields = ('idgroupe_etudiant', 'nomgroupe_etudiant')
        labels = {
            'idgroupe_etudiant': _('ID groupe étudiant'),
            'nomgroupe_etudiant': _('Nom groupe étudiant'),
        }