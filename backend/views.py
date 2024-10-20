from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .forms import ContatoForm

def home(request):
    return render(request, "home.html")

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
