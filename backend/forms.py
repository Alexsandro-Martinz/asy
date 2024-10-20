from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sua mensagem', 'rows': 4}),
        }
