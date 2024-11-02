# views.py
from django.shortcuts import get_object_or_404, redirect, render

from backend.forms.profile_form import ProfileForm
from backend.models.profile_model import Profile


# Criar um novo perfil
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')  # Redireciona para a lista de perfis
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {'form': form})

# Atualizar um perfil existente
def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_form.html', {'form': form})

# View para listar os perfis
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'profile_confirm_delete.html', {'profile': profile})