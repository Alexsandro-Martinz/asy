from gc import get_freeze_count
import profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from backend.forms.paciente_form import PacienteForm
from backend.forms.profile_form import ProfileForm
from backend.forms.user_form import UserForm
from backend.models.paciente_model import Paciente


@login_required
def paciente_delete(request, id):
    try:
        paciente = Paciente.objects.get(pk=id)
        paciente.delete()
        messages.success(request, "Paciente excluído com sucesso!")
    except Paciente.DoesNotExist:
        messages.error(request, "Paciente não encontrado.")
    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao excluir o paciente: {str(e)}")
    return redirect('paciente_list')

@login_required
def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/paciente_list.html', {'pacientes': pacientes})

@login_required
def paciente_create(request):

    if request.method == 'POST':
        user_form_instance = UserForm(request.POST)
        paciente_form_instance = PacienteForm(request.POST)
        
        forms = [
            user_form_instance,
            paciente_form_instance
        ]
        
        for form in forms:
            if not form.is_valid():
                messages.add_message(request, messages.ERROR, form.errors.as_text())     
                return render(request, 'paciente/paciente_create.html', {'forms': forms})

        new_user = user_form_instance.save()
        new_paciente = paciente_form_instance.save(commit=False)
        new_paciente.user = new_user
        new_paciente.save()
        print(new_paciente)
        messages.add_message(request, messages.SUCCESS, "Paciente salvo com sucesso!")
        return redirect("paciente_list")
    
    context = {
        'forms' : [
            UserForm(),
            PacienteForm()
        ],
    }
    return render(request, 'paciente/paciente_create.html', context)


@login_required
def paciente_detail(request, id):
    try:
        paciente = Paciente.objects.get(pk=id)
    except Paciente.DoesNotExist:
        messages.add_message(request, messages.ERROR, "Paciente não encontrado.")
        return redirect('paciente_list')
    except Exception as e:
        messages.add_message(request, messages.ERROR, f"Ocorreu um erro ao carregar o paciente: {str(e)}")
        return redirect('paciente_list')
    return render(request, 'paciente/paciente_detail.html', {'paciente': paciente})


@login_required
def paciente_update(request, id):
    paciente = Paciente.objects.get(pk=id)
    
    if request.method == 'POST':
        paciente_form_instance = PacienteForm(request.POST, instance=paciente)
        
        if not paciente_form_instance.is_valid():
            messages.add_message(request, messages.ERROR, paciente_form_instance.errors.as_text())     
            return render(request, 'paciente/paciente_update.html', {'form': paciente_form_instance})

        paciente_form_instance.save()
        messages.add_message(request, messages.SUCCESS, "Paciente salvo com sucesso!")
        return redirect("paciente_list")
    
    form = PacienteForm(instance=paciente)
    
    return render(request, 'paciente/paciente_update.html', {'form': form, 'birth_date': paciente.birth_date.isoformat()})