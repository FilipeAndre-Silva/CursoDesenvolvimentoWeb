from django.db import models


class Autor(models.Model):

    class Meta:
        verbose_name_plural = "Autores"

    nome_completo = models.CharField(verbose_name="Autor", max_length=30)
    email = models.EmailField(verbose_name="E-mail")