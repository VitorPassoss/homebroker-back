from apps.saidas.models.saida import Saida
from apps.saidas.models.destinacao import Destinacao
from rest_framework import serializers




class SaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saida
        fields = '__all__'




class DestinacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinacao
        fields = '__all__'


class SaidaSerializerRead(serializers.ModelSerializer):
    destinacao = DestinacaoSerializer()
    class Meta:
        model = Saida
        fields = '__all__'
