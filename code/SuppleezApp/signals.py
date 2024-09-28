from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Demandes, ArchiveDemandeTraite, ArchiveDemandeSupprime

@receiver(post_save, sender=Demandes)
def archive_demande_on_status_change(sender, instance, **kwargs):
    """
    Signal handler to archive a Demandes instance when its status changes to 'Approuvé' or 'Refusé'.
    Creates an ArchiveDemandeTraite instance and deletes the original Demandes instance.
    """
    if  instance.statut_demande in ['Approuvé', 'Refusé']:
    
        ArchiveDemandeTraite.objects.create(
            professeur=instance.professeur, cours=instance.cours, cours_optionnel=instance.cours_optionnel,
            confirmation_Pour_cours_optionnel=instance.confirmation_Pour_cours_optionnel, suppleant=instance.suppleant,
            Motif=instance.Motif, imputation=instance.imputation, cpo=instance.cpo,
            Accord_suppleant=instance.Accord_suppleant, remarque=instance.remarque, num_poste=instance.num_poste,
            salaire=instance.salaire, Accord_CF=instance.Accord_CF, date_soumission=instance.date_soumission,
            statut_demande=instance.statut_demande
        )
        instance.delete()

@receiver(pre_delete, sender=Demandes)
def archive_demande_before_delete(sender, instance, **kwargs):
    """
    Signal handler to archive a Demandes instance before deletion.
    Creates an ArchiveDemandeSupprime instance if the status is not 'Approuvé' or 'Refusé'.
    """
    if instance.statut_demande not in ['Approuvé', 'Refusé']:
    
        ArchiveDemandeSupprime.objects.create(
            professeur=instance.professeur, cours=instance.cours, cours_optionnel=instance.cours_optionnel,
            confirmation_Pour_cours_optionnel=instance.confirmation_Pour_cours_optionnel, suppleant=instance.suppleant,
            Motif=instance.Motif, imputation=instance.imputation, cpo=instance.cpo,
            Accord_suppleant=instance.Accord_suppleant, remarque=instance.remarque, num_poste=instance.num_poste,
            salaire=instance.salaire, Accord_CF=instance.Accord_CF, date_soumission=instance.date_soumission,
            statut_demande=instance.statut_demande
        )

@receiver(pre_delete, sender=ArchiveDemandeTraite)
def archive_demande_traite_before_delete(sender, instance, **kwargs):
    """
    Signal handler to archive an ArchiveDemandeTraite instance before deletion.
    Creates an ArchiveDemandeSupprime instance.
    """
    if instance.statut_demande in ['Approuvé', 'Refusé']:
    
        ArchiveDemandeSupprime.objects.create(
            professeur=instance.professeur, cours=instance.cours, cours_optionnel=instance.cours_optionnel,
            confirmation_Pour_cours_optionnel=instance.confirmation_Pour_cours_optionnel, suppleant=instance.suppleant,
            Motif=instance.Motif, imputation=instance.imputation, cpo=instance.cpo,
            Accord_suppleant=instance.Accord_suppleant, remarque=instance.remarque, num_poste=instance.num_poste,
            salaire=instance.salaire, Accord_CF=instance.Accord_CF, date_soumission=instance.date_soumission,
            statut_demande=instance.statut_demande
        )
