from django.db import models
from apps.producao.models.producao import Producao
from apps.saidas.models.destinacao import Destinacao
from django.utils import timezone


class Saida(models.Model):
    destinacao = models.ForeignKey(Destinacao, on_delete=models.CASCADE, null=True)
    producao = models.ForeignKey(Producao, on_delete=models.CASCADE, null=True, blank=True)
    dt_saida = models.DateTimeField(default=timezone.now)



    class Meta:
        ordering = ['-dt_saida'] 