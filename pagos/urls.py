from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pagos, name='lista_pagos'),
    path('generar-cuotas/', views.generar_cuotas, name='generar_cuotas'),
    path('cuota/<int:cuota_id>/pagar/', views.registrar_pago, name='registrar_pago'),
    path('recordatorios/', views.enviar_recordatorios, name='enviar_recordatorios'),
]
