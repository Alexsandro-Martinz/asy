from django.contrib.auth.models import User
from django.db import models


class MedicoEspecialidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    crm = models.CharField(max_length=10)
    especialidades = models.ManyToManyField(MedicoEspecialidade)
    data_de_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.get_full_name()


    