from django.contrib import admin
from .models import Projetos, Funcionarios


# Register your models here.
@admin.register(Funcionarios)
class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cargo')


@admin.register(Projetos)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome_projeto', 'descricao', 'data_inicio', 'data_final', 'gerente_projeto', 'imagem', 'ferramentas')