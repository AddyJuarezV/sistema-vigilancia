from django.db import models


class Vivienda(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    calle = models.CharField(max_length=100, blank=True)
    seccion = models.CharField(max_length=50, blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.numero


class Residente(models.Model):
    vivienda = models.ForeignKey(
        Vivienda,
        on_delete=models.CASCADE,
        related_name="residentes"
    )

    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"