from backend.models.paciente_model import Paciente
from django.db.models import Q


class PacienteServices:

    PAGINATE_PER_PAGE = 10

    def __init__(self):
        pass

    def get_paginated_bounds(self, page):
        page = int(page)
        start = (page - 1) * self.PAGINATE_PER_PAGE
        end = start + self.PAGINATE_PER_PAGE
        return start, end

    def is_search_valid(self, search):
        return search is not None and search != ""

    def get_all_pacientes(self, page):
        start, end = self.get_paginated_bounds(page)
        return Paciente.objects.all()[start:end]

    def get_paciente_by_id(self, id):
        return Paciente.objects.get(pk=id)

    def get_pacientes_by_name(self, search, page):
        start, end = self.get_paginated_bounds(page)
        return Paciente.objects.filter(
            Q(first_name__contains=search) | Q(last_name__contains=search)
        )[start:end]
