from django.urls import path
from . import views

urlpatterns = [
    path("viviendas/", views.lista_viviendas, name="lista_viviendas"),
    path("viviendas/nueva/", views.registrar_vivienda, name="registrar_vivienda"),

    path("residentes/", views.lista_residentes, name="lista_residentes"),
    path("residentes/nuevo/", views.registrar_residente, name="registrar_residente"),
]