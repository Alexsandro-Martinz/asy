from django.contrib import admin

from backend.models.MedicoModel import Medico, MedicoEspecialidade
from backend.models.PacienteModel import Paciente
from backend.models.ProntuarioModel import Prontuario

admin.site.site_header = 'Asilo'
admin.site.site_title = 'Asilo'

admin.site.index_title = 'Administração'

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Prontuario)
admin.site.register(MedicoEspecialidade)
