from backend.models.paciente_model import Paciente
from django.db.models import Q


class PacienteServices:
    def __init__(self):
        pass

    def is_search_valid(self, search):
        return search is not None and search != ""

    def get_all_pacientes(self):
        return Paciente.objects.all()

    def get_paciente_by_id(self, id):
        return Paciente.objects.get(pk=id)

    def get_pacientes_by_name(self, search):
        return Paciente.objects.filter(
            Q(first_name__contains=search) | Q(last_name__contains=search)
        )
