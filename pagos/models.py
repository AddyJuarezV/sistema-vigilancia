from django.conf import settings
from django.db import models
from residentes.models import Residente, Vivienda


class Cuota(models.Model):
    ESTADOS = [('PENDIENTE', 'Pendiente'), ('PAGADO', 'Pagado'), ('VENCIDO', 'Vencido')]
    vivienda = models.ForeignKey(Vivienda, on_delete=models.PROTECT, related_name='cuotas')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto = models.DecimalField(max_digits=9, decimal_places=2)
    estado = models.CharField(max_length=12, choices=ESTADOS, default='PENDIENTE')
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_inicio', 'vivienda__numero']
        constraints = [
            models.UniqueConstraint(fields=['vivienda', 'fecha_inicio', 'fecha_fin'], name='cuota_unica_vivienda_semana')
        ]

    def __str__(self):
        return f'{self.vivienda} · {self.fecha_inicio:%d/%m/%Y} · {self.get_estado_display()}'


class Pago(models.Model):
    METODOS = [('EFECTIVO', 'Efectivo'), ('TRANSFERENCIA', 'Transferencia')]
    cuota = models.OneToOneField(Cuota, on_delete=models.PROTECT, related_name='pago')
    residente = models.ForeignKey(Residente, on_delete=models.SET_NULL, null=True, blank=True, related_name='pagos')
    monto = models.DecimalField(max_digits=9, decimal_places=2)
    metodo = models.CharField(max_length=15, choices=METODOS)
    referencia = models.CharField(max_length=100, blank=True)
    comprobante = models.ImageField(upload_to='comprobantes/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    registrado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='pagos_registrados')

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'Pago {self.cuota.vivienda} · ${self.monto}'
