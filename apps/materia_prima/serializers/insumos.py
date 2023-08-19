from rest_framework import serializers
from apps.materia_prima.models.insumos import Insumos


class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumos
        fields = "__all__"