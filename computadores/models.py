from django.db import models

# Create your models here.

class Maquinas(models.Model):
    TIPO = (('PCP', 'DESKTOP'),('NOT', 'NOTEBOOK'),)
    tipo = models.CharField(max_length=3, choices=TIPO, blank=False, null=False, default='PCP')
    nome_pc = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    processador = models.CharField(max_length=20)
    ano_compra = models.CharField(max_length=5)
    service_tag = models.CharField(max_length=15)
    memoria_ram = models.CharField(max_length=10)
    armazenamento = models.CharField(max_length=10) 
    STATUS = (('DSP', 'Disponivel'), ('OCP', 'Ocupado'),)
    status = models.CharField(max_length=15, choices=STATUS, blank=False, null=False, default='Disponivel' )


    class Meta:
        verbose_name_plural = "Maquina" 

    def __str__(self):
        return self.nome_pc