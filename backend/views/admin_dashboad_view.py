from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from backend.models.medico_model import Medico
from backend.models.paciente_model import Paciente
from backend.models.profile_model import Profile
from backend.models.prontuario_model import Prontuario


# Dashboard para Administradores
@login_required
def dashboard_admin(request):
    amount_pacientes = Paciente.objects.count()
    amount_medicos = Medico.objects.filter(profile__is_superuser=False).count()
    consultas_agendadas = Prontuario.objects.filter(data_consulta__gte=date.today()).count()
    usuarios = Profile.objects.filter(is_superuser=False)

    context = {
        'amount_pacientes': amount_pacientes,
        'amount_medicos': amount_medicos,
        'consultas_agendadas': consultas_agendadas,
        'usuarios': usuarios,
    }
    return render(request, 'dashboard_admin.html', context)

