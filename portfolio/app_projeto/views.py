from django.shortcuts import render, redirect
from .forms import ProjetosModelForm
from .models import Projetos

# Create your views here.
def index(request):
    return render(request, 'index.html')


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


def projetos_visualizar(request, nome_projeto):
    dados = {}

    form = ProjetosModelForm(request.POST, request.FILES or None)
    projeto = Projetos.objects.get(nome_projeto=nome_projeto)
    dados['projeto'] = projeto
    dados['form'] = form
    return render(request, 'projetos_visualizar.html', dados)


def excluir_projeto(request, pk):
    dados = {}

    projeto = Projetos.objects.get(pk=pk)
    dados['projeto'] = projeto
    projeto.delete()
    return redirect('projetos')
