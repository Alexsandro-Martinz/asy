from random import choice, choices, randint
from django.contrib.auth.models import User
from faker import Faker
from regex import P

from backend.forms.user_form import UserForm
from backend.models.paciente_model import Paciente
from .forms.paciente_form import PacienteForm
from cpf_generator import CPF
import datetime

f = Faker()


def run():
    print("Starting Populate Database")
    for _ in range(100):
        user = User.objects.create_user(
            f.email(), "password", first_name=f.first_name(), last_name=f.last_name()
        )
        user.save()
        paciente = Paciente.objects.create(
            user=user,
            phone_number=f.phone_number(),
            first_name=f.first_name(),
            last_name=f.last_name(),
            email=f.email(),
            cpf=CPF.generate(),
            rg=f.random_number(digits=8),
            birth_date=datetime.date.today(),
            address=f.address(),
            estado_civil=choice(list(Paciente.ESTADO_CIVIL_CHOICES.values())),
            genero=choice(list(Paciente.GENERO_CHOICES.values())),
            nome_responsavel=f.name(),
            telefone_responsavel=f.phone_number(),
            grau_parentesco=choice(list(Paciente.PARENTESCO_CHOICES.values())),
        )
        paciente.save()

    print("Finished Populate Database")


run()
