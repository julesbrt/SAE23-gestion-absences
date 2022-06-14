# Generated by Django 4.0.5 on 2022-06-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absences',
            fields=[
                ('idabsences', models.IntegerField(db_column='idAbsences', primary_key=True, serialize=False)),
                ('jutsificationcours', models.IntegerField(db_column='JutsificationCours')),
                ('docjustcours', models.CharField(db_column='DocjustCours', max_length=255)),
            ],
            options={
                'db_table': 'absences',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('idcours', models.IntegerField(primary_key=True, serialize=False)),
                ('titrecours', models.CharField(db_column='TitreCours', max_length=45)),
                ('datecours', models.DateField(db_column='DateCours')),
                ('dureecours', models.CharField(db_column='DureeCours', max_length=45)),
            ],
            options={
                'db_table': 'cours',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enseignants',
            fields=[
                ('idenseignants', models.IntegerField(db_column='idEnseignants', primary_key=True, serialize=False)),
                ('nomenseignants', models.CharField(db_column='NomEnseignants', max_length=45)),
                ('prenomenseignants', models.CharField(db_column='PrenomEnseignants', max_length=45)),
                ('emailenseignants', models.CharField(db_column='EmailEnseignants', max_length=45)),
            ],
            options={
                'db_table': 'enseignants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Etudiants',
            fields=[
                ('idetudiants', models.IntegerField(primary_key=True, serialize=False)),
                ('nometudiants', models.CharField(db_column='NomEtudiants', max_length=25)),
                ('prenometudiant', models.CharField(db_column='PrenomEtudiant', max_length=25)),
                ('emailetudiant', models.CharField(db_column='EmailEtudiant', max_length=45)),
                ('photoetudiant', models.CharField(db_column='PhotoEtudiant', max_length=255)),
            ],
            options={
                'db_table': 'etudiants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupeEtudiant',
            fields=[
                ('idgroupe_etudiant', models.IntegerField(db_column='idGroupe-etudiant', primary_key=True, serialize=False)),
                ('nomgroupe_etudiant', models.CharField(db_column='nomGroupe-etudiant', max_length=45)),
            ],
            options={
                'db_table': 'groupe-etudiant',
                'managed': False,
            },
        ),
    ]