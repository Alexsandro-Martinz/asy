from django import forms

from backend.models.contact_model import Contact


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('nome', 'email', 'mensagem')
        labels = {
            'nome': 'Nome',
            'email': 'Email',
            'mensagem': 'Mensagem',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        