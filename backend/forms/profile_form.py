# forms.py

from django import forms

from ..models.profile_model import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user_type', 'phone_number', 'first_name', 'last_name', 'email', 
            'cpf', 'rg', 'birth_date', 'address', 'estado_civil', 'genero'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
