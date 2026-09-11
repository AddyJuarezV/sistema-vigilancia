from django.contrib import admin
from .models import Vivienda, Residente


@admin.register(Vivienda)
class ViviendaAdmin(admin.ModelAdmin):
    list_display = ("numero", "calle", "seccion", "activa")
    search_fields = ("numero", "calle", "seccion")


@admin.register(Residente)
class ResidenteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido_paterno",
        "apellido_materno",
        "vivienda",
        "telefono",
        "correo",
        "activo",
    )

    search_fields = (
        "nombre",
        "apellido_paterno",
        "apellido_materno",
        "correo",
        "telefono",
    )

    list_filter = ("activo", "vivienda")
