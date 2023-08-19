from rest_framework import serializers
from apps.materia_prima.models.entrada import Entrada
from apps.materia_prima.serializers.fornecedores import FornecedoresSerializer
from apps.materia_prima.serializers.insumos import InsumosSerializer

class EntradaSerializer(serializers.ModelSerializer):
    fornecedor = FornecedoresSerializer()
    tipo_insumo = InsumosSerializer()

    class Meta:
        model = Entrada
        fields = ['fornecedor','tipo_insumo','quantidade','valor','id','created_at']


class EntradaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = ['fornecedor','tipo_insumo','quantidade','valor','id', 'created_at']
