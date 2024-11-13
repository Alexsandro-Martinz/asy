from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from backend.models.medico_model import Medico
from backend.models.paciente_model import Paciente
from backend.models.prontuario_model import Prontuario


# Dashboard para Administradores
@login_required
def dashboard_admin(request):
    paciente_qtd = Paciente.objects.count()
    print(paciente_qtd)
    medico_qtd = Medico.objects.filter().count()
    consultas_agendadas_qtd = Prontuario.objects.filter(data_consulta__gte=date.today()).count()
    cards = [
        {'title': 'Total de Pacientes', 'value': paciente_qtd, 'url': "/paciente_list"},
        {'title': 'Total de Profissionais', 'value': medico_qtd},
        {'title': 'Consultas Agendadas', 'value': consultas_agendadas_qtd},
        {'title': 'Consultas de Hoje', 'value': Prontuario.objects.filter(data_consulta=date.today()).count()}
    ]
    return render(request, 'dashboard_admin.html', {'cards': cards})

