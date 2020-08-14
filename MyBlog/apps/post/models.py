from django.db import models

from django.utils import timezone

# Create your models here.

class Post(models.Model):
    titulo_post = models.CharField(verbose_name ='Título do Post', max_length=200)
    nome_autor = models.CharField(verbose_name ='Nome do Autor', max_length=50,)
    email_autor = models.EmailField(verbose_name ='E-mail para contato com Autor', max_length=50, default=None)
    data_publicacao = models.DateTimeField(verbose_name ='Data de Publicação', default=timezone.now)
    postagem = models.TextField(verbose_name ='Postagem', max_length=500, default=None)
