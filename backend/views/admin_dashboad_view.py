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
    medico_qtd = Medico.objects.filter().count()
    consultas_agendadas_qtd = Prontuario.objects.filter(data_consulta__gte=date.today()).count()
    cards = [
        {'title': 'Pacientes', 'subtitle': f'Total: {paciente_qtd}', 'url': '/paciente/list'},
        {'title': 'Medicos', 'subtitle': f'Total: {medico_qtd}', 'url': '/medico/list'},
        {'title': 'Prontuários', 'subtitle': f'Total: {consultas_agendadas_qtd}'},
    ]
    return render(request, 'dashboard_admin.html', {'cards': cards})

