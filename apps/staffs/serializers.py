

from rest_framework import serializers
from apps.staffs.models import *


class StatusSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Status
        fields = "__all__"

class EmpresaSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Empresas
        fields = "__all__"


class CargoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Cargos
        fields = "__all__"

class TurnoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Turnos
        fields = "__all__"

class FechamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fechamentos
        fields = "__all__"

class ProfissionaisSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    empresa = EmpresaSerializer()
    cargo = CargoSerializer()
    turnos = TurnoSerializer()

    class Meta:
        model = Profissional
        fields = [
            'nome',
            'cpf',
            'contato_email',
            'saldo_atual',
            'user_id',
            ]




class ProfissionalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = [
            'nome',
            'pis',
            'jornada',
            'turnos',
            'contato_phone',
            'contato_email',
            'cpf',
            'empresa', 
            'status', 
            'cargo', 
            'dt_nascimento', 
            'dt_entrada', 
            'dt_saida', 
            'custo_beneficios', 
            'custo_salario', 
            'custo_bruto']


class FechamentosCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fechamentos
        fields = [
            'empresa',
            'dia',
            'valor_final',
            'valor_inicial',
            'valorizacao',
            'porcentagem'
            ]


class CarteiraSerializer(serializers.ModelSerializer):   
    empresa = EmpresaSerializer();

    class Meta:
        model = Carteira
        fields = "__all__"
    
class PersonSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Person
        fields = "__all__"
    
class PersonCreateSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Person
        fields = "__all__"

class CarteiraCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carteira
        fields = ('id', 'empresa', 'valor_compra', 'valor_venda', 'valor_acao', 'quantidade', 'person')

    def create(self, validated_data):
        empresa = validated_data['empresa']
        person_instance = validated_data['person']  
        valor_compra = validated_data['valor_compra']
        quantidade = validated_data['quantidade']
        valor_acao = validated_data['valor_acao']
        person = Person.objects.get(id=person_instance.id)  


        if person.saldo_atual < valor_compra:
            raise serializers.ValidationError('Saldo insuficiente.')
        

        valor_compra_sum = Carteira.objects.filter(empresa=empresa, person=person).aggregate(models.Sum('valor_compra'))['valor_compra__sum'] or 0
        quantidade_sum = Carteira.objects.filter(empresa=empresa, person=person).aggregate(models.Sum('quantidade'))['quantidade__sum'] or 0

        wallet, created = Carteira.objects.update_or_create(
            empresa=empresa,
            person=person,
            defaults={
                'valor_compra': valor_compra_sum + valor_compra,
                'quantidade': quantidade_sum + quantidade,
                'valor_acao': valor_acao
            }
        )

        person.saldo_atual -= valor_compra
        person.save()

        return wallet
