from datetime import date

from django.db import models


class Profile(models.Model):
    
    MASCULINO = 'masculino'
    FEMININO = 'feminino'
    OUTRO = 'outro'
    
    GENERO_CHOICES = {
        MASCULINO : 'Masculino',
        FEMININO : 'Feminino',
        OUTRO : 'Outro',
    }
    
    CASADO = 'casado'
    SOLTEIRO = 'solteiro'
    DIVORCIADO = 'divorciado'
    VIUVO = 'viuvo'
    UNIAO_ESTAVEL = 'uniao estavel'
    
    ESTADO_CIVIL_CHOICES = {
        CASADO : 'Casado',
        SOLTEIRO : 'Solteiro',
        DIVORCIADO : 'Divorciado',
        VIUVO : 'Viuvo',
        UNIAO_ESTAVEL : 'Uniao Estavel',
    }
    
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(default="")
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, unique=True, blank=True, null=True, default='Sem RG cadastrado')
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True, default='Não informado')
    estado_civil = models.CharField(max_length=50, choices=ESTADO_CIVIL_CHOICES, blank=True, null=True)
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES, blank=True, null=True, default=GENERO_CHOICES[OUTRO])

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()
    
    def get_age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
