

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

class ProfissionaisSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    empresa = EmpresaSerializer()
    cargo = CargoSerializer()
    turnos = TurnoSerializer()

    class Meta:
        model = Profissional
        fields = "__all__"

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