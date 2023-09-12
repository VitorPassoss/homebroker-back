from django.contrib import admin
from apps.materia_prima.models.entrada import Entrada
from apps.materia_prima.models.estoque_insumo import EstoqueInsumo


    

class EntradaAdmin(admin.ModelAdmin):
    search_fields = ['fornecedor']
    list_display = ['fornecedor_name', 'quantidade', 'tipo_insumo_name', 'valor', 'created_at']

    def fornecedor_name(self, obj):
        return obj.fornecedor.nome
    fornecedor_name.short_description = 'Fornecedor'

    def tipo_insumo_name(self, obj):
        return obj.tipo_insumo.nome
    tipo_insumo_name.short_description = 'Tipo de Insumo'


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['tipo_insumo_nome', 'quantidade', 'valor', 'valor', 'created_at']

    def tipo_insumo_nome(self, obj):
        return obj.tipo_insumo.nome
    tipo_insumo_nome.short_description = 'Tipo Insumo'





admin.site.register(Entrada, EntradaAdmin)
admin.site.register(EstoqueInsumo, EstoqueAdmin)
