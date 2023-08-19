from django.db import models


TIPO_GRANDEZA = [("Un", "Unidade"), ("Kg", "kilograma"), ("L", "litros")]




class TipoProduto(models.Model):
    nome = models.CharField(max_length=255)



class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    grandeza = models.CharField(
        max_length=4, choices=TIPO_GRANDEZA
    )
    codigo = models.CharField(max_length=255)
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE, null=True)
    validade = models.DateTimeField(auto_now_add=True)