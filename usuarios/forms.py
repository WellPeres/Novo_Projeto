from dataclasses import fields
from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = (
            'nome', 'setor' ,'contrato', 'computador', 'user_login', 'email', 'equipamento_em_uso',  'monitor_em_uso', 
            )