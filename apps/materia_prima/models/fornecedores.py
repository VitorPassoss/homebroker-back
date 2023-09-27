from django.db import models


class Fornecedores(models.Model):
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(
        verbose_name="CPF/CNPJ",
        max_length=14,
        blank=True,
        null=True
    )
    razao_social = models.CharField(max_length=255)
    contato = models.CharField(max_length=255,  blank=True, null=True)
