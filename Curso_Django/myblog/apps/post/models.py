from django.db import models
from apps.autor.models import Autor


class Post(models.Model):
    titulo = models.CharField(verbose_name="Título do Post", max_length=50)
    conteudo = models.TextField(verbose_name="Conteúdo do Post", max_length=200)
    autor = models.ForeignKey(Autor, verbose_name='Autor', on_delete=models.CASCADE)
    publicacao = models.DateTimeField(auto_now=True, verbose_name='Data de Publicação')

