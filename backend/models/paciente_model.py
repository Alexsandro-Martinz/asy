
import faker
from cpf_generator import CPF
from django.db import models

from backend.models.profile_model import Profile


class Paciente(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    nome_responsavel = models.CharField(max_length=255, blank=True, null=True)
    telefone_responsavel = models.CharField(max_length=20, blank=True, null=True)
    grau_parentesco = models.CharField(max_length=100, blank=True, null=True)
    
    # Informações Médicas
    doencas_cronicas = models.TextField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)
    medicamentos = models.TextField(blank=True, null=True)
    cirurgias = models.TextField(blank=True, null=True)
    historico_internacoes = models.TextField(blank=True, null=True)
    vacinas = models.TextField(blank=True, null=True)
    exames = models.TextField(blank=True, null=True)
    
    # Informações de Estado Cognitivo e Comportamental
    condicoes_cognitivas = models.TextField(blank=True, null=True)
    alteracoes_humor = models.TextField(blank=True, null=True)
    comportamento_social = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


def paciente_populate_a_100():
    fake = faker.Faker("pt_BR")
    for i in range(100):
        profile = Profile.objects.create(
            user_type=Profile.USER_TYPE_CHOICES[0]["patient"],
            username=f"paciente{i+1}",
            password="123456",
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            cpf=CPF.generate(),
        )
        Paciente.objects.create(profile=profile)

    print("Pacientes populados com sucesso!")
