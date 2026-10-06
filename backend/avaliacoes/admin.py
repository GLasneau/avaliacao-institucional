from django.contrib import admin

from .models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("aluno", "disciplina", "nota", "status", "data_criacao")
    list_filter = ("status", "disciplina")
    search_fields = ("aluno__nome", "disciplina__nome")
