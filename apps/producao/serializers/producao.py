from rest_framework import serializers
from apps.producao.models.producao import Producao, ProducaoInsumo, ProducaoItem
from apps.materia_prima.models.estoque_insumo import EstoqueInsumo
from apps.materia_prima.serializers.insumos import InsumosSerializer
from apps.producao.serializers.produtos import ProdutosSerializer
from decimal import Decimal


class ProducaoInsumoReadSerializer(serializers.ModelSerializer):
    tipo_insumo = InsumosSerializer()
    class Meta:
        model = ProducaoInsumo
        fields = '__all__'

class ProducaoItemReadSerializer(serializers.ModelSerializer):
    produto = ProdutosSerializer()
    class Meta:
        model = ProducaoItem
        fields = '__all__'

class ProducaoInsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducaoInsumo
        fields = '__all__'

class ProducaoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducaoItem
        fields = '__all__'

class ProducaoSerializerRead(serializers.ModelSerializer):
    insumos = ProducaoInsumoReadSerializer(source='producaoinsumo_set', many=True)
    produtos = ProducaoItemReadSerializer(source='producaoitem_set', many=True)
    
    class Meta:
        model = Producao
        fields = ['status', 'quantidade', 'valor', 'created_at', 'insumos', 'produtos']


class ProducaoSerializer(serializers.ModelSerializer):
    insumos = ProducaoInsumoSerializer(many=True, write_only=True)
    produtos = ProducaoItemSerializer(many=True, write_only=True)

    class Meta:
        model = Producao
        fields = ['status', 'quantidade', 'valor', 'created_at', 'insumos', 'produtos']

    def create(self, validated_data):
        insumos_data = validated_data.pop('insumos')
        produtos_data = validated_data.pop('produtos')
        
        producao = Producao.objects.create(**validated_data)

        for insumo_data in insumos_data:
            self.update_stock(insumo_data)
            ProducaoInsumo.objects.create(producao=producao, **insumo_data)
        for produto_data in produtos_data:
            ProducaoItem.objects.create(producao=producao, **produto_data)

        return producao

    def update_stock(self, insumo):
        if(insumo['tipo_insumo'] != 'Leite'):
            search_item  = EstoqueInsumo.objects.get(tipo_insumo_id=insumo['tipo_insumo'])
            insumo_quantidade = Decimal(insumo['quantidade'])
            print(insumo_quantidade)
            search_item.quantidade = search_item.quantidade -  insumo_quantidade
            return search_item.save()
        

        
        