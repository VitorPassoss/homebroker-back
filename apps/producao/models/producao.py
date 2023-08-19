from django.db import models
from apps.producao.models.produtos import Produtos
from django.utils import timezone

STATUS = [("EA", "Em andamento"), ("F", "Finalizado")]

class Producao(models.Model):
    status = models.CharField(
        max_length=2, choices=STATUS
    )
    quantidade = models.DecimalField(
        max_digits=21, decimal_places=3, blank=True, null=True
    )
    valor = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
        

    class Meta:
        ordering = ['-created_at'] 

class ProducaoItem(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, null=True)
    producao = models.ForeignKey(Producao, on_delete=models.CASCADE, null=True)
    quantidade = models.DecimalField(
        max_digits=21, decimal_places=3, blank=True, null=True
    )
    valor = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-created_at'] 
    