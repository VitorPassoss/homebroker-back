# apps/staffs/admin.py

from django.contrib import admin
from .models import Fechamentos, Empresas

class FechamentoAdmin(admin.ModelAdmin):
    search_fields = ['dia', 'empresa__name']  # Search by 'dia' and 'name' of 'Empresas'
    list_display = ['empresa', 'dia', 'valor_inicial', 'valor_final', 'variação', 'porcentagem']
    list_filter = ['empresa'] 
    ordering = ['dia']  

admin.site.register(Fechamentos, FechamentoAdmin)
