from django.db import models


TIPO_GRANDEZA = [("Un", "Unidade"), ("Kg", "kilograma"), ("L", "litros")]



class Insumos(models.Model):
    nome = models.CharField(max_length=255)
    grandeza = models.CharField(
        max_length=4, choices=TIPO_GRANDEZA
    )

