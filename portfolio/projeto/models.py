from django.db import models
from stdimage.models import StdImageField

# Create your models here.
class Funcionarios(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'


class Projetos(models.Model):
    nome_projeto = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_final = models.DateField()
    gerente_projeto = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)
    imagem = StdImageField('Imagem', upload_to='projetos', variations={'thumb': (124, 124)})
    ferramentas = models.TextField()

    def __str__(self) -> str:
        return self.nome_projeto