from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('reportes/', views.reportes, name='reportes'),
    path('reportes/pagos.csv', views.exportar_pagos_csv, name='exportar_pagos_csv'),
]
