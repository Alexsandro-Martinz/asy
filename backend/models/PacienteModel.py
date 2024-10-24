from django.db import models

class Paciente(models.Model):
    # Dados Pessoais
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    idade = models.PositiveIntegerField()
    genero = models.CharField(max_length=50, blank=True, null=True)
    estado_civil = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    
    # Dados do Responsável
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
