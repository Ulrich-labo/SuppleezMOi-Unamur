# Generated by Django 5.0.2 on 2024-04-01 18:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuppleezApp', '0008_alter_archivedemandesupprime_date_soumission_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivedemandesupprime',
            options={'verbose_name_plural': 'Demandes supprimées'},
        ),
        migrations.AlterModelOptions(
            name='archivedemandetraite',
            options={'verbose_name_plural': 'Demandes traitées'},
        ),
        migrations.AlterField(
            model_name='archivedemandesupprime',
            name='Accord_CF',
            field=models.CharField(choices=[('', 'Sélectionnez une option'), ('Oui', 'Oui'), ('Non', 'Non')], default='Sélectionnez une option', max_length=200),
        ),
        migrations.AlterField(
            model_name='archivedemandesupprime',
            name='confirmation_Pour_cours_optionnel',
            field=models.CharField(choices=[('', 'Sélectionnez une option'), ('Oui', 'Oui'), ('Non', 'Non')], default='Sélectionnez une option', max_length=200),
        ),
        migrations.AlterField(
            model_name='archivedemandesupprime',
            name='date_soumission',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='archivedemandesupprime',
            name='statut_demande',
            field=models.CharField(choices=[('En cours de traitement', ' Était en cours de traitement'), ('Approuvé', 'Approuvé'), ('Refusé', 'Refusé')], default=' Était en cours de traitement', max_length=200),
        ),
        migrations.AlterField(
            model_name='archivedemandetraite',
            name='Accord_CF',
            field=models.CharField(choices=[('', 'Sélectionnez une option'), ('Oui', 'Oui'), ('Non', 'Non')], default='Sélectionnez une option', max_length=200),
        ),
        migrations.AlterField(
            model_name='archivedemandetraite',
            name='confirmation_Pour_cours_optionnel',
            field=models.CharField(choices=[('', 'Sélectionnez une option'), ('Oui', 'Oui'), ('Non', 'Non')], default='Sélectionnez une option', max_length=200),
        ),
        migrations.AlterField(
            model_name='archivedemandetraite',
            name='date_soumission',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='demandes',
            name='Accord_CF',
            field=models.CharField(choices=[('', 'Sélectionnez une option'), ('Oui', 'Oui'), ('Non', 'Non')], default='Sélectionnez une option', max_length=200),
        ),
        migrations.AlterField(
            model_name='demandes',
            name='confirmation_Pour_cours_optionnel',
            field=models.CharField(choices=[('', 'Sélectionnez une option'), ('Oui', 'Oui'), ('Non', 'Non')], default='Sélectionnez une option', max_length=200),
        ),
        migrations.AlterField(
            model_name='demandes',
            name='date_soumission',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
