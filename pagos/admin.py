from django.contrib import admin
from .models import Cuota, Pago

@admin.register(Cuota)
class CuotaAdmin(admin.ModelAdmin):
    list_display = ('vivienda', 'fecha_inicio', 'fecha_fin', 'monto', 'estado')
    list_filter = ('estado', 'fecha_inicio')
    search_fields = ('vivienda__numero',)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('cuota', 'monto', 'metodo', 'fecha', 'registrado_por')
    list_filter = ('metodo', 'fecha')
    search_fields = ('cuota__vivienda__numero', 'referencia')
