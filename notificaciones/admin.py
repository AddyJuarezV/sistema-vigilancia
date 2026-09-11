from django.contrib import admin
from .models import Aviso, Notificacion

@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'fecha', 'activo')
    list_filter = ('tipo', 'activo')
    search_fields = ('titulo', 'mensaje')

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('residente', 'aviso', 'enviada', 'fecha_envio')
    list_filter = ('enviada',)
    search_fields = ('residente__nombre', 'residente__apellido_paterno', 'aviso__titulo')
