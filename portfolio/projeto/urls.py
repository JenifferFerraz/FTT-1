from django.urls import path
from .views import index, projetos, novo_projeto, excluir_projeto

urlpatterns = [
    path('', index, name='index'),
    path('projetos/', projetos, name='projetos'),
    path('novo-projeto/', novo_projeto, name='novo-projeto'),
    path('excluir-projeto/<int:pk>/', excluir_projeto, name='excluir_projeto'),
]