from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel, name='panel_servicios'),
    path('nuevo/', views.nuevo_servicio, name='nuevo_servicio'),
    path('paqueteria/nueva/', views.nueva_paqueteria, name='nueva_paqueteria'),
    path('servicio/<int:pk>/salida/', views.salida_servicio, name='salida_servicio'),
    path('paqueteria/<int:pk>/salida/', views.salida_paqueteria, name='salida_paqueteria'),
    path('historial/', views.historial, name='historial_servicios'),
]
