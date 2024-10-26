from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from backend.models.MedicoModel import Medico
from backend.models.PacienteModel import Paciente
from backend.models.ProntuarioModel import Prontuario

from .forms import ContatoForm


def dashboard(request):
    """View rendering the dashboard for the user type."""

    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('dashboard_admin')
        else:
            return redirect('dashboard_profissional')
    else:
        return redirect('login')

def index(request):
    return render(request, "index.html")

def saiba_mais(request):
    return render(request, 'sobre.html')

def contato(request):
    """
    View to handle the contact form.
    """
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Check if the form is valid before sending the email
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            # Prevent null pointer references
            if nome and email and mensagem:
                form.save()
                messages.success(request, 'Sua mensagem foi enviada com sucesso!')
                return redirect('contato')
            else:
                # Handle the exception when the form is not valid
                messages.error(request, 'Preencha todos os campos corretamente!')
    else:
        form = ContatoForm()

    return render(request, 'contato.html', {'form': form})


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
    except AttributeError as e:  # Null pointer reference end prevent superuser from accessing dashboard
        messages.error(request, 'Erro ao acessar o dashboard. Verifique se o profissional está cadastrado corretamente.')
        return redirect('/')
    except Exception as e:  # Unhandled exception
        messages.error(request, 'Erro inesperado ao acessar o dashboard. Erro: {}'.format(e))
        return redirect('/')

# Dashboard para Administradores
@login_required
def dashboard_admin(request):
    total_pacientes = Paciente.objects.count()
    total_profissionais = User.objects.filter(is_superuser=False).count()
    consultas_agendadas = Prontuario.objects.filter(data_consulta__gte=date.today()).count()
    usuarios = User.objects.filter(is_superuser=False)

    context = {
        'total_pacientes': total_pacientes,
        'total_profissionais': total_profissionais,
        'consultas_agendadas': consultas_agendadas,
        'usuarios': usuarios,
    }
    return render(request, 'dashboard_admin.html', context)

