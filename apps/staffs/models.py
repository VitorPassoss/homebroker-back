from django.db import models

# Create your models here.
from django.db import models

class Empresas(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(
        verbose_name="cnpj",
        max_length=14,
        blank=True,
        null=True
    )
    contato = models.CharField(max_length=255,  blank=True, null=True)

class Status(models.Model):
    nome = models.CharField(max_length=255)

class Cargos(models.Model):
    nome = models.CharField(max_length=255)

class Turnos(models.Model):
    nome = models.CharField(max_length=255)

from django.db import models


class Profissional(models.Model):
    nome = models.CharField(max_length=255)
    pis = models.CharField(max_length=255)
    jornada = models.CharField(max_length=255)
    turnos = models.ForeignKey(Turnos, on_delete=models.CASCADE, null=True)
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=14,
        blank=True,
        null=True
    )
    contato_phone = models.CharField(max_length=255, blank=True, null=True)
    contato_email = models.CharField(max_length=255, blank=True, null=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE, null=True)
    dt_nascimento = models.DateTimeField(blank=True, null=True)
    dt_entrada = models.DateTimeField(blank=True, null=True)
    dt_saida = models.DateTimeField(blank=True, null=True)
    custo_beneficios = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    custo_salario = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    custo_bruto = models.DecimalField(max_digits=19, decimal_places=2, null=True)



   


