from cProfile import label

from django import forms

from backend.models.profile_model import Profile
    

class ProfileForm(forms.ModelForm):
    title = "Informações Pessoais"
    class Meta:
        model = Profile
        fields = ('phone_number', 'first_name', 'last_name', 'birth_date'
                  , 'email', 'cpf', 'rg', 'birth_date', 'address', 'estado_civil', 'genero')

        widget = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'input_format': '%d-%m-%Y'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'birth_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
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
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(cpf) != 11 or not cpf.isdigit():
            raise forms.ValidationError('CPF deve ter 11 digitos')
        return cpf
