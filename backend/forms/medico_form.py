from django import forms

from backend.models.medico_model import Medico


class MedicoForm(forms.ModelForm):
    title = "Informações Pessoais"
    class Meta:
        model = Medico
        exclude = ('user',)
        fields = (
            'phone_number', 'first_name', 'last_name',
            'email', 'cpf', 'rg', 'birth_date', 'address',
            'estado_civil','genero',
            'crm', 'especialidades'
            
        )
        labels = {
            'phone_number': 'Telefone',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'cpf': 'CPF',
            'rg': 'RG',
            'birth_date': 'Data de Nascimento',
            'address': 'Endereço',
            'estado_civil': 'Estado Civil',
            'genero': 'Gênero',
        }
    
