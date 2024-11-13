import faker
from cpf_generator import CPF
from django.db import models

from backend.models.profile_model import Profile


class MedicoEspecialidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nome
    

class Medico(Profile):
    crm = models.CharField(max_length=10)
    especialidades = models.ManyToManyField(MedicoEspecialidade)

    def __str__(self):
        return self.profile.get_full_name()
    

