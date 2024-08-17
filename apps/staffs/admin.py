from django.contrib import admin
from .models import Fechamentos, Empresas, Carteira, Person

class EmpresasAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome', 'cnpj', 'contato']

class FechamentoAdmin(admin.ModelAdmin):
    search_fields = ['dia', 'empresa__nome']  # Ensure 'empresa__nome' is a valid field
    list_display = ['empresa', 'dia', 'valor_inicial', 'valor_final', 'variação', 'porcentagem']
    list_filter = ['empresa']
    ordering = ['dia']

class CarteiraAdmin(admin.ModelAdmin):
    search_fields = ['person__nome']
    
    def person_nome(self, obj):
        return obj.person.nome
    person_nome.admin_order_field = 'person__nome'
    person_nome.short_description = 'Person Name'
    
    def empresa_nome(self, obj):
        return obj.empresa.nome
    empresa_nome.admin_order_field = 'empresa__nome'
    empresa_nome.short_description = 'Empresa Name'
    
    list_display = ['person_nome', 'empresa_nome', 'valor_compra', 'valor_venda', 'valor_acao', 'quantidade']

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'cpf']
    
    def user_nome(self, obj):
        return obj.user_id.username  # Assuming you want the username; change if needed
    user_nome.admin_order_field = 'user_id__username'
    user_nome.short_description = 'User Name'
    
    list_display = ['nome', 'cpf', 'contato_email', 'saldo_atual', 'user_nome']

# Conditional registration
if not admin.site.is_registered(Empresas):
    admin.site.register(Empresas, EmpresasAdmin)

admin.site.register(Fechamentos, FechamentoAdmin)
admin.site.register(Carteira, CarteiraAdmin)
admin.site.register(Person, PersonAdmin)
