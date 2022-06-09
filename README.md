# SAE23-gestion-absences

#  Ce sujet va vous permettre de fournir une interface de gestion des absences du département. Le gestionnaires pourra saisir les absences à différents cours et saisir par la suite une justification Le schéma de données est le suivant

des groupes d'étudiants (id, nom)
des étudiants (id, nom, prénom, email, groupe, photo)
des enseignants (id, nom, prénom, email)
des cours (id, titre du cours, date, enseignant, durée, groupe)
des absences à des cours (étudiants, cours, justifié ou non, justification)
Vous devez implémenter un CRUD pour chacun de ces types de données. vous préparerez la base en avance et la remplirez avec des groupes, des étudiants et des enseignants.
Votre site web devra permettre la saisie de nouveaux cours et d'absences à ce cours. Vous devrez aussi pouvoir valider l'absence et insérer des justificatifs . Vous devrez aussi pouvoir insérer les absences d'un cours  l'aide d'un fichier. La structure du fichier attendu devra bien sur être décrite soit dans une aide, soit en préambule de la page de chargement.

Vous devrez être à même de pouvoir générer une fiche de liste des absences d'un cours. Vous pourrez aussi générer la listes des absences d'un étudiant avec le total justifié et non justifié de ses absences. 
