import faker
from cpf_generator import CPF
from django.db import models

from backend.models.profile_model import Profile


class MedicoEspecialidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    

class Medico(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    crm = models.CharField(max_length=10)
    especialidades = models.ManyToManyField(MedicoEspecialidade)

    def __str__(self):
        return self.profile.get_full_name()
    


def populate_medicos(apps, sc):
    fake = faker.Faker("pt_BR")
    Medico.objects.all().delete()
    for i in range(10):
        profile = Profile.objects.create(
            user_type="MEDICO",
            username=f"medico{i+1}",
            password="123456",
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            cpf=CPF.generate(),
        )
        crm = fake.numerify(text="##########")
        Medico.objects.create(profile=profile, crm=crm)
