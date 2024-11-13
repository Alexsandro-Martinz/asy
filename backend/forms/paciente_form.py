from django import forms

from backend.models.paciente_model import Paciente


class PacienteForm(forms.ModelForm):
    title = "Informações Pessoais"
    class Meta:
        model = Paciente
        exclude = ('user',)
        fields = (
            'phone_number', 'first_name', 'last_name', 'email', 'cpf', 'rg', 'birth_date', 'address', 'estado_civil', 'genero',
            'nome_responsavel',
            'telefone_responsavel',
            'grau_parentesco',
            'doencas_cronicas',
            'alergias',
            'medicamentos',
            'cirurgias',
            'historico_internacoes',
            'vacinas',
            'exames',
            'condicoes_cognitivas',
            'alteracoes_humor',
            'comportamento_social',
        )
        labels = {
            'nome_responsavel': 'Nome do Responsável',
            'telefone_responsavel': 'Telefone do Responsável',
            'grau_parentesco': 'Grau de Parentesco',
            'doencas_cronicas': 'Doenças Crônicas',
            'alergias': 'Alergias',
            'medicamentos': 'Medicamentos',
            'cirurgias': 'Cirurgias Anteriores',
            'historico_internacoes': 'Histórico de Internações',
            'vacinas': 'Vacinas Tomadas',
            'exames': 'Exames Realizados',
            'condicoes_cognitivas': 'Condições Cognitivas',
            'alteracoes_humor': 'Alterações de Humor',
            'comportamento_social': 'Comportamento Social',
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
    
