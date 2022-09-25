from django.db import models

# Create your models here.

class Monitor(models.Model):
    MONITOR = (('Monitor1', 'Monitor1'),('Monitor2', 'Monitor2'),)
    monitor = models.CharField(max_length=10, choices=MONITOR, blank=False, null=False, default='Monitor1')
    marca_monitor = models.CharField(max_length=10, default='Dell')
    modelo = models.CharField(max_length=30, default='E1916' )
    service_tag = models.CharField(max_length=30)
    polegadas = models.CharField(max_length=30)

    monitor2 = models.CharField(max_length=10, choices=MONITOR, blank=False, null=False, default='Monitor2')
    marca_monitor2 = models.CharField(max_length=10, default='Dell')
    modelo2 = models.CharField(max_length=30, default='E1916' )
    service_tag2 = models.CharField(max_length=30)
    polegadas2 = models.CharField(max_length=30)


    class Meta:
        verbose_name_plural = "Monitor"

    def __str__(self):
        return self.modelo