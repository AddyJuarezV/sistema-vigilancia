from django.urls import path
from . import views

urlpatterns = [
    path('', views.activos, name='accesos_activos'),
    path('nuevo/', views.registrar, name='registrar_acceso'),
    path('<int:pk>/salida/', views.salida, name='salida_acceso'),
    path('historial/', views.historial, name='historial_accesos'),
]
