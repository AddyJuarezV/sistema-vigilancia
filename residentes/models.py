from decimal import Decimal
from django.db import models


class Vivienda(models.Model):
    numero = models.CharField(max_length=20, unique=True, verbose_name='Número')
    calle = models.CharField(max_length=100, blank=True)
    seccion = models.CharField(max_length=50, blank=True, verbose_name='Sección')
    cuota_semanal = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('150.00'))
    activa = models.BooleanField(default=True)

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return self.numero


class Residente(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE, related_name='residentes')
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(max_length=100, blank=True, verbose_name='Apellido materno')
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    correo = models.EmailField(blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['apellido_paterno', 'nombre']

    @property
    def nombre_completo(self):
        return ' '.join(filter(None, [self.nombre, self.apellido_paterno, self.apellido_materno]))

    def __str__(self):
        return f'{self.nombre_completo} · {self.vivienda.numero}'
