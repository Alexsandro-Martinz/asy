from math import e

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from backend.forms.paciente_form import PacienteForm
from backend.forms.profile_form import ProfileForm
from backend.forms.user_form import UserForm
from backend.models.paciente_model import Paciente


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
                return redirect('paciente_create', {'forms': forms})

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
    return render(request, 'paciente/paciente_form.html', context)