from rest_framework import serializers
from apps.materia_prima.models.estoque_insumo import EstoqueInsumo
from apps.materia_prima.serializers.insumos import InsumosSerializer

class EstoqueSerializer(serializers.ModelSerializer):
    tipo_insumo = InsumosSerializer()

    class Meta:
        model = EstoqueInsumo
        fields = '__all__'

