from django import forms 
from .models import Projetos


class ProjetosModelForm(forms.ModelForm):
    class Meta:
        model = Projetos
        fields = ['nome_projeto', 'descricao', 'data_inicio', 'data_final', 'gerente_projeto', 'imagem', 'ferramentas']