from django.db import models
from computadores.models import Maquinas
from monitores.models import Monitor

# Create your models here.

class Usuario(models.Model):
    CONTRATO = (('CLT', 'CLT'), ('PJ', 'Pessoa Juridica'), ('EST', 'Estágiario'),)
    contrato = models.CharField(max_length=3, choices= CONTRATO, blank=False, null=False, default='CLT')
    COMPUTADOR = (('PCP', 'Desktop'), ('NOT', 'Notebook'),('PTC', 'Particular'),)
    computador = models.CharField(max_length=3, choices=COMPUTADOR, blank=False, null=False, default='PCP')
    nome = models.CharField(max_length=50)
    user_login = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    setor = models.CharField(max_length=30)
    equipamento_em_uso = models.ForeignKey(Maquinas, default=1, verbose_name="Equipamento", on_delete=models.SET_DEFAULT)
    monitor_em_uso = models.ForeignKey(Monitor, default=1, related_name="Monitor_Estoque", verbose_name="Monitores", on_delete=models.SET_DEFAULT)


    def __str__(self):
        return self.nome