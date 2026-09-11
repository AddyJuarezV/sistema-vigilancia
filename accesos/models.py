from django.conf import settings
from django.db import models
from residentes.models import Vivienda


class AccesoVisitante(models.Model):
    IDENTIFICACIONES = [
        ('INE', 'INE'), ('PASAPORTE', 'Pasaporte'), ('LICENCIA', 'Licencia'), ('OTRA', 'Otra')
    ]
    nombre = models.CharField(max_length=160, verbose_name='Nombre del visitante')
    vivienda = models.ForeignKey(Vivienda, on_delete=models.PROTECT, related_name='visitas')
    motivo = models.CharField(max_length=200, blank=True)
    tipo_identificacion = models.CharField(max_length=20, choices=IDENTIFICACIONES, verbose_name='Identificación presentada')
    identificacion_verificada = models.BooleanField(default=True, verbose_name='Identificación verificada')
    vehiculo = models.CharField(max_length=100, blank=True, help_text='Marca / modelo')
    color = models.CharField(max_length=50, blank=True)
    placas = models.CharField(max_length=20, blank=True)
    entrada = models.DateTimeField(auto_now_add=True)
    salida = models.DateTimeField(null=True, blank=True)
    guardia = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='accesos_registrados')
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ['-entrada']

    @property
    def dentro(self):
        return self.salida is None

    def __str__(self):
        return f'{self.nombre} → {self.vivienda.numero}'
