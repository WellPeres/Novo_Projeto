from django.contrib import admin
from .models import Usuario
from computadores.models import Maquinas
from monitores.models import Monitor

# Register your models here.

class ListaUsuario(admin.ModelAdmin):
    list_display = ('id', 'nome', 'setor' ,'contrato', 'computador', 'user_login', 'email', 'equipamento_em_uso',  'monitor_em_uso')
    search_fields = ( 'nome', 'setor' ,'contrato', 'computador', 'user_login', 'email', 'equipamento_em_uso',  'monitor_em_uso')
    list_display_links = ('nome', 'equipamento_em_uso', 'monitor_em_uso')

admin.site.register(Usuario, ListaUsuario)

