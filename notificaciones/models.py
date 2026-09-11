from django.db import models
from residentes.models import Residente


class Aviso(models.Model):
    TIPOS = [
        ("BASURA", "Camión de basura"),
        ("AGUA", "Pipa de agua"),
        ("GAS", "Gas"),
        ("MANTENIMIENTO", "Mantenimiento"),
        ("GENERAL", "Aviso general"),
    ]

    tipo = models.CharField(max_length=30, choices=TIPOS)
    titulo = models.CharField(max_length=150)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Notificacion(models.Model):
    residente = models.ForeignKey(
        Residente,
        on_delete=models.CASCADE,
        related_name="notificaciones"
    )
    aviso = models.ForeignKey(
        Aviso,
        on_delete=models.CASCADE,
        related_name="notificaciones"
    )
    enviada = models.BooleanField(default=False)
    fecha_envio = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.residente} - {self.aviso}"