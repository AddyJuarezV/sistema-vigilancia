from django.conf import settings
from django.db import models
from residentes.models import Vivienda


class Servicio(models.Model):
    TIPOS = [
        ('PLOMERIA', 'Plomería'), ('ELECTRICIDAD', 'Electricidad'), ('INTERNET', 'Internet'),
        ('GAS', 'Gas'), ('JARDINERIA', 'Jardinería'), ('MANTENIMIENTO', 'Mantenimiento'),
        ('CONSTRUCCION', 'Construcción'), ('MUDANZA', 'Mudanza'), ('OTRO', 'Otro'),
    ]
    tipo = models.CharField(max_length=30, choices=TIPOS)
    persona_empresa = models.CharField(max_length=160, verbose_name='Persona o empresa')
    vivienda = models.ForeignKey(Vivienda, on_delete=models.PROTECT, related_name='servicios_recibidos')
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    vehiculo = models.CharField(max_length=100, blank=True)
    placas = models.CharField(max_length=20, blank=True)
    entrada = models.DateTimeField(auto_now_add=True)
    salida = models.DateTimeField(null=True, blank=True)
    guardia = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='servicios_registrados')
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ['-entrada']

    @property
    def dentro(self):
        return self.salida is None

    def __str__(self):
        return f'{self.get_tipo_display()} · {self.persona_empresa}'


class Paqueteria(models.Model):
    EMPRESAS = [
        ('AMAZON', 'Amazon'), ('MERCADO_LIBRE', 'Mercado Libre'), ('DHL', 'DHL'),
        ('FEDEX', 'FedEx'), ('ESTAFETA', 'Estafeta'), ('UPS', 'UPS'), ('OTRO', 'Otro'),
    ]
    empresa = models.CharField(max_length=30, choices=EMPRESAS)
    repartidor = models.CharField(max_length=160, blank=True)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.PROTECT, related_name='paqueterias')
    vehiculo = models.CharField(max_length=100, blank=True)
    placas = models.CharField(max_length=20, blank=True)
    entrada = models.DateTimeField(auto_now_add=True)
    salida = models.DateTimeField(null=True, blank=True)
    guardia = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='paqueterias_registradas')
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ['-entrada']

    @property
    def dentro(self):
        return self.salida is None

    def __str__(self):
        return f'{self.get_empresa_display()} → {self.vivienda.numero}'
