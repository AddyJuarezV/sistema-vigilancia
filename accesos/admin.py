from django.contrib import admin
from .models import AccesoVisitante

@admin.register(AccesoVisitante)
class AccesoVisitanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'vivienda', 'placas', 'entrada', 'salida', 'guardia')
    search_fields = ('nombre', 'placas', 'vivienda__numero')
    list_filter = ('tipo_identificacion', 'entrada')
