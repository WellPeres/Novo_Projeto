from django.contrib import admin
from .models import Maquinas

# Register your models here.

class ListaMaquinas(admin.ModelAdmin):
    list_display = ('id','tipo', 'nome_pc', 'modelo', 'processador', 'ano_compra', 'service_tag', 'memoria_ram', 'armazenamento', 'status',)
    search_fields = ('tipo', 'nome_pc', 'modelo', 'processador', 'ano_compra', 'service_tag', 'memoria_ram', 'armazenamento', 'status',)
    list_display_links = ('nome_pc', 'modelo', 'service_tag')

admin.site.register(Maquinas, ListaMaquinas)