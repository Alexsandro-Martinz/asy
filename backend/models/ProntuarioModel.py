from django.db import models

from backend.models.MedicoModel import Medico
from backend.models.PacienteModel import Paciente

class Prontuario(models.Model):
    # Relacionamentos
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    
    # Dados da Consulta
    data_consulta = models.DateField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    tratamento_recomendado = models.TextField(blank=True, null=True)
    
    # Informações Adicionais
    exames_solicitados = models.TextField(blank=True, null=True)
    medicamentos_prescritos = models.TextField(blank=True, null=True)
    encaminhamentos = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Prontuário de {self.paciente.nome} - {self.data_consulta}"
