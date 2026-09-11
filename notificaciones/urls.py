from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_avisos, name="lista_avisos"),
    path("nuevo/", views.crear_aviso, name="crear_aviso"),
]