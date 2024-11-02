from django.shortcuts import get_object_or_404, redirect, render

from backend.forms.medico_form import MedicoForm

from ..models.medico_model import Medico


# Listar médicos
def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medico_list.html', {'medicos': medicos})

# Criar um novo médico
def medico_create(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm()
    return render(request, 'medico_form.html', {'form': form})

# Atualizar um médico
def medico_update(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'medico_form.html', {'form': form})

# Excluir um médico
def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect('medico_list')
    return render(request, 'medico_confirm_delete.html', {'medico': medico})
