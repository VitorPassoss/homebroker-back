from django.db import models
from apps.producao.models.producao import Producao
from apps.saidas.models.destinacao import Destinacao
from django.utils import timezone


class Saida(models.Model):
    destinacao = models.ForeignKey(Destinacao, on_delete=models.CASCADE, null=True)
    id_ref = models.CharField(max_length=255)
    ref =  models.CharField(max_length=255)
    dt_saida = models.DateTimeField(default=timezone.now)
    quantidade = models.DecimalField(
        max_digits=21, decimal_places=3, blank=True, null=True
    )
    class Meta:
        ordering = ['-dt_saida'] 