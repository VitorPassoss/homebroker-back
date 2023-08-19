from django.db import models


class Destinacao(models.Model):
    nome = models.CharField(max_length=255)
    