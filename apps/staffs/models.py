from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Empresas(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(
        verbose_name="cnpj",
        max_length=14,
        blank=True,
        null=True
    )
    contato = models.CharField(max_length=255,  blank=True, null=True)
    status = models.BooleanField(default=True)  

    def __str__(self):
        return self.nome

class Fechamentos(models.Model):
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE, null=True)
    dia = models.CharField(max_length=255, blank=True, null=True)
    valor_final = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    valor_inicial = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    variação = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    porcentagem = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.empresa} - {self.dia}"

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



class Person(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=14,
        blank=True,
        null=True
    )
    contato_email = models.CharField(max_length=255, blank=True, null=True)
    saldo_atual = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Carteira(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE, null=True)
    valor_compra = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    valor_venda = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    valor_acao = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    quantidade = models.DecimalField(max_digits=19, decimal_places=2, null=True)


class Pagamentos(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    id_pagamento = models.ForeignKey(Empresas, on_delete=models.CASCADE, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=2, null=True)

