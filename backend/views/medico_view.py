from django.shortcuts import render
from backend.forms.medico_form import MedicoForm
from backend.forms.user_form import UserForm
from backend.models.medico_model import Medico
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render


@login_required
def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/medico_list.html', {'medicos': medicos})

@login_required
def medico_create(request):

    if request.method == 'POST':
        user_form_instance = UserForm(request.POST)
        medico_form_instance = MedicoForm(request.POST)
        forms = [
            user_form_instance,
            medico_form_instance
        ]
        
        for form in forms:
            if not form.is_valid():
                messages.add_message(request, messages.ERROR, form.errors.as_text())     
                return redirect('medico_create', {'forms': forms})

        new_user = user_form_instance.save()
        new_medico = medico_form_instance.save(commit=False)
        new_medico.user = new_user
        new_medico.save()
        messages.add_message(request, messages.SUCCESS, "Medico salvo com sucesso!")
        return redirect("medico_list")
    
    context = {
        'forms' : [
            UserForm(),
            MedicoForm()
        ],
    }
    return render(request, 'medico/medico_create.html', context)