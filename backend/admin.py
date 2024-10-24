from django.contrib import admin

from backend.models.ProfissionalSaudeModel import ProfissionalSaude


@admin.register(ProfissionalSaude)
class ProfissionalSaudeAdmin(admin.ModelAdmin):
    pass
