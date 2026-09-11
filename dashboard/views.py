import csv
import json
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from accounts.decorators import administrador_required
from accesos.models import AccesoVisitante
from pagos.models import Cuota, Pago
from residentes.models import Residente, Vivienda
from servicios.models import Paqueteria, Servicio


@login_required
def inicio(request):
    hoy = timezone.localdate()
    inicio_semana = hoy - timedelta(days=hoy.weekday())
    fin_semana = inicio_semana + timedelta(days=6)
    total_semana = Pago.objects.filter(fecha__date__range=(inicio_semana, fin_semana)).aggregate(total=Sum('monto'))['total'] or 0

    labels, datos = [], []
    for retroceso in range(3, -1, -1):
        ini = inicio_semana - timedelta(weeks=retroceso)
        fin = ini + timedelta(days=6)
        labels.append(f'{ini:%d/%m}')
        datos.append(float(Pago.objects.filter(fecha__date__range=(ini, fin)).aggregate(total=Sum('monto'))['total'] or 0))

    context = {
        'recaudado_semana': total_semana,
        'pagos_pendientes': Cuota.objects.filter(estado__in=['PENDIENTE', 'VENCIDO']).count(),
        'visitantes_hoy': AccesoVisitante.objects.filter(entrada__date=hoy).count(),
        'servicios_dentro': Servicio.objects.filter(salida__isnull=True).count() + Paqueteria.objects.filter(salida__isnull=True).count(),
        'viviendas': Vivienda.objects.filter(activa=True).count(),
        'residentes': Residente.objects.filter(activo=True).count(),
        'labels_recaudacion': json.dumps(labels),
        'datos_recaudacion': json.dumps(datos),
        'pagados': Cuota.objects.filter(estado='PAGADO').count(),
        'no_pagados': Cuota.objects.exclude(estado='PAGADO').count(),
        'accesos_activos': AccesoVisitante.objects.filter(salida__isnull=True).select_related('vivienda')[:5],
    }
    return render(request, 'dashboard/inicio.html', context)


@administrador_required
def reportes(request):
    return render(request, 'dashboard/reportes.html', {
        'pagos': Pago.objects.select_related('cuota__vivienda', 'registrado_por')[:100],
        'accesos': AccesoVisitante.objects.select_related('vivienda', 'guardia')[:100],
        'servicios': Servicio.objects.select_related('vivienda', 'guardia')[:100],
    })


@administrador_required
def exportar_pagos_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="pagos.csv"'
    response.write('\ufeff')
    w = csv.writer(response)
    w.writerow(['Vivienda', 'Semana', 'Monto', 'Método', 'Fecha', 'Registró'])
    for p in Pago.objects.select_related('cuota__vivienda', 'registrado_por'):
        w.writerow([p.cuota.vivienda.numero, p.cuota.fecha_inicio, p.monto, p.get_metodo_display(), p.fecha, p.registrado_por.username])
    return response
