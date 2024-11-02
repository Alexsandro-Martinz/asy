from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    
    ADMIN = 'admin'
    DOCTOR = 'doctor'
    PATIENT = 'patient'
    
    USER_TYPE_CHOICES = {
        ADMIN : 'Administrator',
        DOCTOR : 'Doctor',
        PATIENT : 'Patient',
    }
    
    MASCULINO = 'masculino'
    FEMININO = 'feminino'
    OUTRO = 'outro'
    
    GENERO_CHOICES = {
        MASCULINO : 'Masculino',
        FEMININO : 'Feminino',
        OUTRO : 'Outro',
    }
    
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    email = models.EmailField(default="")
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, unique=True, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    estado_civil = models.CharField(max_length=50, blank=True, null=True)
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES, blank=True, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name
    
    def get_age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
