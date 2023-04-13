from django.shortcuts import render, redirect
from .forms import ProjetosModelForm
from .models import Projetos

def index(request):
    dados = {}
    dados['projetos'] = Projetos.objects.all()
    return render(request, 'index.html', dados)


def projetos(request):
    dados = {}
    dados['projetos'] = Projetos.objects.all()
    return render(request, 'projetos.html', dados)


def novo_projeto(request):
    if str(request.user) != 'AnonymousUser':
        dados = {}
        form = ProjetosModelForm(request.POST, request.FILES or None)
        
        if form.is_valid():
            form.save()
            return redirect('projetos')

        dados['form'] = form
        return render(request, 'novo-projeto.html', dados)
    else:
        return redirect('index')

def excluir_projeto(request, pk):
    dados = {}

    projeto = Projetos.objects.get(pk=pk)
    dados['projeto'] = projeto
    projeto.delete()
    return redirect('projetos')
