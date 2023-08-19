from rest_framework import serializers
from apps.materia_prima.models.fornecedores import Fornecedores


class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = "__all__"