from django.db import models
from django.contrib.auth.models import User

# Administrador do Sistema
class Administrador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50, default='Administrador')

    def __str__(self):
        return self.usuario.username