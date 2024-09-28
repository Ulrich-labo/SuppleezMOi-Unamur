# Generated by Django 5.0.2 on 2024-02-21 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuppleezApp', '0005_alter_demandes_date_soumission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivedemandesupprime',
            name='cours_optionnel',
            field=models.CharField(choices=[('', 'Sélectionnez une option'), ('Oui', 'Oui'), ('Non', 'Non')], default='Sélectionnez une option', max_length=200),
        ),
        migrations.AlterField(
            model_name='archivedemandesupprime',
            name='date_soumission',
            field=models.DateField(default=datetime.datetime(2024, 2, 21, 19, 42, 45, 843389, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='archivedemandesupprime',
            name='statut_demande',
            field=models.CharField(choices=[('En cours de traitement', 'était en cours de traitement'), ('Approuvé', 'Approuvé'), ('Refusé', 'Refusé')], default='était en cours de traitement', max_length=200),
        ),
        migrations.AlterField(
            model_name='archivedemandetraite',
            name='cours_optionnel',
            field=models.CharField(choices=[('', 'Sélectionnez une option'), ('Oui', 'Oui'), ('Non', 'Non')], default='Sélectionnez une option', max_length=200),
        ),
        migrations.AlterField(
            model_name='archivedemandetraite',
            name='date_soumission',
            field=models.DateField(default=datetime.datetime(2024, 2, 21, 19, 42, 45, 842747, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='demandes',
            name='cours_optionnel',
            field=models.CharField(choices=[('', 'Sélectionnez une option'), ('Oui', 'Oui'), ('Non', 'Non')], default='Sélectionnez une option', max_length=200),
        ),
        migrations.AlterField(
            model_name='demandes',
            name='date_soumission',
            field=models.DateField(default=datetime.datetime(2024, 2, 21, 19, 42, 45, 842059, tzinfo=datetime.timezone.utc)),
        ),
    ]
