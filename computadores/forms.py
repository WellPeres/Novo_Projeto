from dataclasses import fields
from django import forms

from .models import Maquinas

class MaquinaForm(forms.ModelForm):

    class Meta:
        model = Maquinas
        fields = ('tipo', 'nome_pc', 'modelo', 'processador', 'ano_compra',
         'service_tag', 'memoria_ram', 'armazenamento', 'status',)