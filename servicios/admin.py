from django.contrib import admin
from .models import Paqueteria, Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'persona_empresa', 'vivienda', 'placas', 'entrada', 'salida')
    list_filter = ('tipo', 'entrada')
    search_fields = ('persona_empresa', 'placas', 'vivienda__numero')

@admin.register(Paqueteria)
class PaqueteriaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'repartidor', 'vivienda', 'placas', 'entrada', 'salida')
    list_filter = ('empresa', 'entrada')
    search_fields = ('repartidor', 'placas', 'vivienda__numero')
