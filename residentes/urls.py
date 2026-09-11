from django.urls import path
from . import views

urlpatterns = [
    path('viviendas/', views.lista_viviendas, name='lista_viviendas'),
    path('viviendas/nueva/', views.registrar_vivienda, name='registrar_vivienda'),
    path('viviendas/<int:pk>/editar/', views.editar_vivienda, name='editar_vivienda'),
    path('residentes/', views.lista_residentes, name='lista_residentes'),
    path('residentes/nuevo/', views.registrar_residente, name='registrar_residente'),
    path('residentes/<int:pk>/editar/', views.editar_residente, name='editar_residente'),
]
