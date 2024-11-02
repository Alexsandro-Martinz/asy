from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from backend.models.medico_model import Medico
from backend.models.prontuario_model import Prontuario


# Dashboard para Profissionais de Saúde
@login_required
def medico_dashboard(request):
    
    user = getattr(request, 'user', None)
    medico = Medico.objects.filter(user=user).first()
    if not medico:
        messages.error(request, 'Erro ao acessar o dashboard. Verifique se o profissional está cadastrado corretamente.')
        return redirect('/')
    
    try:
        consultas_hoje = Prontuario.objects.filter(medico=medico, data_consulta=date.today())
        proximas_consultas = Prontuario.objects.filter(medico=medico, data_consulta__gte=date.today()).count()
        pacientes_atendidos = Prontuario.objects.filter(medico=medico).values('paciente').distinct().count()

        context = {
            'consultas_hoje': consultas_hoje,
            'proximas_consultas': proximas_consultas,
            'pacientes_atendidos': pacientes_atendidos,
            'consultas': consultas_hoje,
        }
        return render(request, 'dashboard_profissional.html', context)
    except AttributeError:  # Null pointer reference end prevent superuser from accessing dashboard
        messages.error(request, 'Erro ao acessar o dashboard. Verifique se o profissional está cadastrado corretamente.')
        return redirect('/')
    except Exception as e:  # Unhandled exception
        messages.error(request, 'Erro inesperado ao acessar o dashboard. Erro: {}'.format(e))
        return redirect('/')
