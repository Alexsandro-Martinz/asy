from django.db import models
from django.contrib.auth.models import User

class ProfissionalSaude(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    
    # Contato
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    
    # Dados Profissionais
    CARGO_CHOICES = [
        ('Médico', 'Médico'),
        ('Enfermeiro', 'Enfermeiro'),
        ('Técnico de Enfermagem', 'Técnico de Enfermagem'),
    ]
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)
    registro_profissional = models.CharField(max_length=50, unique=True)  # Ex: CRM, COREN
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    
    # Horários e Disponibilidade
    dias_atendimento = models.CharField(max_length=100)  # Exemplo: "Seg, Ter, Qua"
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def __str__(self):
        return self.nome_completo