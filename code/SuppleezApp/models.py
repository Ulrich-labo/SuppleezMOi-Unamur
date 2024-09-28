from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone
import json

class UserApp(AbstractUser):
    """
    A custom user model for the application
    ...
    Attributes
    ----------
    first_name : str
        the first name of the user
    last_name : str
        the last name of the user
    email : EmailField
        the email address of the user

    Methods
    -------
    __str__(self)
        Return a string representation of the user
    
    Meta
    ----
    verbose_name_plural : str
        the plural name for the model in the admin interface
    """

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        """
        Return a string representation of the user
        """
        return self.first_name + " " + self.last_name
    
    class Meta:
        """
        Meta class for UserApp
        """
        verbose_name_plural = "Professeurs"

class Cours(models.Model):
    """
    A model representing courses in the application
    ...
    Attributes
    ----------
    code : str
        the code of the course
    titre : str
        the title of the course
    Programmes : str
        the programs associated with the course

    Methods
    -------
    __str__(self)
        Return a string representation of the course
    
    Meta
    ----
    verbose_name_plural : str
        the plural name for the model in the admin interface
    """

    code = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    Programmes = models.CharField(max_length=200)

    def __str__(self):
        """
        Return a string representation of the course
        """
        return self.code + " " + self.titre
    
    class Meta:
        """
        Meta class for Cours
        """
        verbose_name_plural = "Cours"
    
class ImputationSalaire(models.Model):
    """
    A model representing possibilities for salary allocation
    ...
    Attributes
    ----------
    imputation : str
        the description of the salary allocation
    
    Methods
    -------
    __str__(self)
        Return a string representation of the salary allocation possibility
    """

    imputation = models.CharField(max_length=500)

    def __str__(self):
        """
        Return a string representation of the salary allocation possibility
        """
        return str(self.imputation)




class Demandes(models.Model):
    """
    A model representing substitution requests
    ...
    Attributes
    ----------
    STATUT_CHOICES : list of tuple
        choices for the status of the request
    OPTION_CHIOCES : list of tuple
        choices for options lectures in the request
    CHOICES_ACCORD_SUPPLEANT : list of tuple
        choices for the agreement with the substitute
    professeur : ForeignKey
        foreign key to the UserApp model representing the professor making the request
    cours : ForeignKey
        foreign key to the Cours model representing the course for the request
    cours_optionnel : str
        option for optional course
    confirmation_Pour_cours_optionnel : str
        confirmation for an optional course
    suppleant : str
        substitute for the professor
    Motif : TextField
        reason for the request
    imputation : ForeignKey
        foreign key to the ImputationSalaire model representing the salary allocation
    cpo : str
        CPO for the request
    Accord_suppleant : str
        agreement with the substitute
    remarque : TextField
        remarks for the request
    num_poste : str
        post number for the request
    salaire : DecimalField
        salary for the request
    Accord_CF : str
        agreement with the CF 
    date_soumission : DateField
        date of submission for the request
    statut_demande : str
        status of the request

    Methods
    -------
    __str__(self)
        Return a string representation of the request
    
    Meta
    ----
    verbose_name_plural : str
        the plural name for the model in the admin interface
    """

    STATUT_CHOICES = [
        ('En cours de traitement', 'En cours de traitement'),
        ('Approuvé', 'Approuvé'),
        ('Refusé', 'Refusé'),
    ]

    OPTION_CHIOCES = [
        ('','Sélectionnez une option'),
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]

    CHOICES_ACCORD_SUPPLEANT = [('', 'Sélectionnez une option'),('Oui', 'Oui'), ('Non', 'Non')]

    professeur = models.ForeignKey(UserApp, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    cours_optionnel = models.CharField(max_length=200, choices=OPTION_CHIOCES, default='Sélectionnez une option')
    confirmation_Pour_cours_optionnel = models.CharField(max_length=200, choices=OPTION_CHIOCES, default='Sélectionnez une option')
    suppleant = models.CharField(max_length=200)
    Motif = models.TextField()
    imputation = models.ForeignKey(ImputationSalaire, on_delete=models.CASCADE)
    cpo = models.CharField(max_length=200, null=True, blank=True)
    Accord_suppleant = models.CharField(max_length=200, choices=CHOICES_ACCORD_SUPPLEANT, default='Sélectionnez une option')
    remarque = models.TextField(null=True, blank=True)
    num_poste = models.CharField(max_length=200, null=True, blank=True)
    salaire = models.DecimalField(default=0, decimal_places=3, max_digits=100, null=True, blank=True)
    Accord_CF = models.CharField(max_length=200, choices=OPTION_CHIOCES, default='Sélectionnez une option')
    date_soumission = models.DateField(default=timezone.now)
    statut_demande = models.CharField(max_length=200, choices=STATUT_CHOICES, default='En cours de traitement')

    def __str__(self):
        """
        Return a string representation of the request
        """
        return str(self.cours)

    class Meta:
        """
        Meta class for Demandes
        """
        verbose_name_plural = "Demandes en cours"

    

class ArchiveDemandeTraite(models.Model):
    """
    A model containing already processed requests
    ...
    Attributes
    ----------
    STATUT_CHOICES : list of tuple
        choices for the status of the request
    OPTION_CHIOCES : list of tuple
        choices for options lectures in the request
    CHOICES_ACCORD_SUPPLEANT : list of tuple
        choices for the agreement with the substitute
    professeur : ForeignKey
        foreign key to the UserApp model representing the professor making the request
    cours : ForeignKey
        foreign key to the Cours model representing the course for the request
    cours_optionnel : str
        option for optional course
    confirmation_Pour_cours_optionnel : str
        confirmation for an optional course
    suppleant : str
        substitute for the professor
    Motif : TextField
        reason for the request
    imputation : ForeignKey
        foreign key to the ImputationSalaire model representing the salary allocation
    cpo : str
        CPO for the request
    Accord_suppleant : str
        agreement with the substitute
    remarque : TextField
        remarks for the request
    num_poste : str
        post number for the request
    salaire : DecimalField
        salary for the request
    Accord_CF : str
        agreement with the CF 
    date_soumission : DateField
        date of submission for the request
    statut_demande : str
        status of the request

    Methods
    -------
    __str__(self)
        Return a string representation of the processed request
    
    Meta
    ----
    verbose_name_plural : str
        the plural name for the model in the admin interface
    """

    STATUT_CHOICES = [
        ('Approuvé', 'Approuvé'),
        ('Refusé', 'Refusé'),
    ]

    OPTION_CHOICES = [
        ('', 'Sélectionnez une option'),
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]

    CHOICES_ACCORD_SUPPLEANT = [('', 'Sélectionnez une option'),('Oui', 'Oui'), ('Non', 'Non')]

    professeur = models.ForeignKey(UserApp, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    cours_optionnel = models.CharField(max_length=200, choices=OPTION_CHOICES, default='Sélectionnez une option')
    confirmation_Pour_cours_optionnel = models.CharField(max_length=200, choices=OPTION_CHOICES, default='Sélectionnez une option')
    suppleant = models.CharField(max_length=200)
    Motif = models.TextField()
    imputation = models.ForeignKey(ImputationSalaire, on_delete=models.CASCADE)
    cpo = models.CharField(max_length=200, null=True, blank=True)
    Accord_suppleant = models.CharField(max_length=200, choices=CHOICES_ACCORD_SUPPLEANT, default='Sélectionnez une option')
    remarque = models.TextField(null=True, blank=True)
    num_poste = models.CharField(max_length=200, null=True, blank=True)
    salaire = models.DecimalField(default=0, decimal_places=3, max_digits=100, null=True, blank=True)
    Accord_CF = models.CharField(max_length=200, choices=OPTION_CHOICES, default='Sélectionnez une option')
    date_soumission = models.DateField(default=timezone.now)
    statut_demande = models.CharField(max_length=200, choices=STATUT_CHOICES, default='En cours de traitement')

    def __str__(self):
        """
        Return a string representation of the processed request
        """
        return str(self.cours)

    class Meta:
        """
        Meta class for ArchiveDemandeTraite
        """
        verbose_name_plural = "Demandes traitées"


class ArchiveDemandeSupprime(models.Model):
    """
    A model containing deleted requests
    ...
    Attributes
    ----------
    STATUT_CHOICES : list of tuple
        choices for the status of the request
    OPTION_CHIOCES : list of tuple
        choices for options lectures in the request
    CHOICES_ACCORD_SUPPLEANT : list of tuple
        choices for the agreement with the substitute
    professeur : ForeignKey
        foreign key to the UserApp model representing the professor making the request
    cours : ForeignKey
        foreign key to the Cours model representing the course for the request
    cours_optionnel : str
        option for optional course
    confirmation_Pour_cours_optionnel : str
        confirmation for an optional course
    suppleant : str
        substitute for the professor
    Motif : TextField
        reason for the request
    imputation : ForeignKey
        foreign key to the ImputationSalaire model representing the salary allocation
    cpo : str
        CPO for the request
    Accord_suppleant : str
        agreement with the substitute
    remarque : TextField
        remarks for the request
    num_poste : str
        post number for the request
    salaire : DecimalField
        salary for the request
    Accord_CF : str
        agreement with the CF 
    date_soumission : DateField
        date of submission for the request
    statut_demande : str
        status of the request

    Methods
    -------
    __str__(self)
        Return a string representation of the deleted request
    
    Meta
    ----
    verbose_name_plural : str
        the plural name for the model in the admin interface
    """
    STATUT_CHOICES = [
        ('En cours de traitement', ' Était en cours de traitement'),
        ('Approuvé', 'Approuvé'),
        ('Refusé', 'Refusé'),
    ]

    OPTION_CHOICES = [
        ('', 'Sélectionnez une option'),
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]

    CHOICES_ACCORD_SUPPLEANT = [('', 'Sélectionnez une option'),('Oui', 'Oui'), ('Non', 'Non')]

    professeur = models.ForeignKey(UserApp, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    cours_optionnel = models.CharField(max_length=200, choices=OPTION_CHOICES, default='Sélectionnez une option')
    confirmation_Pour_cours_optionnel = models.CharField(max_length=200, choices=OPTION_CHOICES, default='Sélectionnez une option')
    suppleant = models.CharField(max_length=200)
    Motif = models.TextField()
    imputation = models.ForeignKey(ImputationSalaire, on_delete=models.CASCADE)
    cpo = models.CharField(max_length=200, null=True, blank=True)
    Accord_suppleant =  models.CharField(max_length =200,choices = CHOICES_ACCORD_SUPPLEANT, default ='Sélectionnez une option')
    remarque = models.TextField(null=True, blank=True)
    num_poste = models.CharField(max_length=200,null=True, blank=True)
    salaire = models.DecimalField(default=0, decimal_places=3, max_digits=100,null=True, blank=True)
    Accord_CF = models.CharField(max_length=200, choices=OPTION_CHOICES, default='Sélectionnez une option')
    date_soumission = models.DateField(default=timezone.now)
    statut_demande = models.CharField(max_length=200, choices=STATUT_CHOICES, default=' Était en cours de traitement')

    def __str__(self):
        return str(self.cours)

    class Meta:
        verbose_name_plural = "Demandes supprimées"