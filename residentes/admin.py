from django.contrib import admin
from .models import Residente, Vivienda

@admin.register(Vivienda)
class ViviendaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'calle', 'seccion', 'cuota_semanal', 'activa')
    search_fields = ('numero', 'calle', 'seccion')
    list_filter = ('activa', 'seccion')

@admin.register(Residente)
class ResidenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'vivienda', 'telefono', 'correo', 'activo')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'correo', 'telefono', 'vivienda__numero')
    list_filter = ('activo', 'vivienda')
