from django.db import models
from apps.materia_prima.models.fornecedores import Fornecedores
from apps.materia_prima.models.insumos import Insumos

class EstoqueInsumo(models.Model):
    tipo_insumo = models.ForeignKey(Insumos, on_delete=models.CASCADE, null=True)
    quantidade = models.DecimalField(
        max_digits=21, decimal_places=3, blank=True, null=True
    )
    valor = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['-created_at'] 