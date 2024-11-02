from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.models.paciente_model import Paciente
from backend.models.profile_model import Profile

from .models.medico_model import Medico


@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == Profile.DOCTOR:
            Medico.objects.create(user=instance)
        elif instance.user_type == Profile.PATIENT:
            Paciente.objects.create(user=instance)