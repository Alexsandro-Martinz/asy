from django.contrib import admin

from backend.models.medico_model import Medico, MedicoEspecialidade
from backend.models.paciente_model import Paciente
from backend.models.profile_model import Profile
from backend.models.prontuario_model import Prontuario

admin.site.site_header = 'Asilo'
admin.site.site_title = 'Asilo'

admin.site.index_title = 'Administração'

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Prontuario)
admin.site.register(MedicoEspecialidade)
admin.site.register(Profile)