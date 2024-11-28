from django.db import models

from backend.models.profile_model import Profile


class Paciente(Profile):

    PAI = "pai"
    MAE = "mae"
    TIO_OR_TIA = "tio(a)"
    FILHO = "filho"
    IRMAO = "irmao(a)"
    AVO = "avo(a)"
    OUTRO = "outro"

    PARENTESCO_CHOICES = {
        PAI: "Pai",
        MAE: "Mae",
        TIO_OR_TIA: "Tio(a)",
        FILHO: "Filho",
        IRMAO: "Irmao(a)",
        AVO: "Avo(a)",
        OUTRO: "Outro",
    }

    nome_responsavel = models.CharField(max_length=255)
    telefone_responsavel = models.CharField(max_length=20)
    grau_parentesco = models.CharField(max_length=100)

    # Informações Médicas
    doencas_cronicas = models.CharField(max_length=255, blank=True, null=True)
    alergias = models.CharField(max_length=255, blank=True, null=True)
    medicamentos = models.CharField(max_length=255, blank=True, null=True)
    cirurgias = models.CharField(max_length=255, blank=True, null=True)
    historico_internacoes = models.CharField(max_length=255, blank=True, null=True)
    vacinas = models.CharField(max_length=255, blank=True, null=True)
    exames = models.CharField(max_length=255, blank=True, null=True)

    # Informações de Estado Cognitivo e Comportamental
    condicoes_cognitivas = models.CharField(max_length=255, blank=True, null=True)
    alteracoes_humor = models.CharField(max_length=255, blank=True, null=True)
    comportamento_social = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
