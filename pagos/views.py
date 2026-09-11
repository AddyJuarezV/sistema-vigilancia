from datetime import timedelta
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from accounts.decorators import administrador_required
from residentes.models import Vivienda
from .forms import PagoForm
from .models import Cuota, Pago
from .services import enviar_confirmacion_pago, enviar_recordatorio_cuota


def semana_actual():
    hoy = timezone.localdate()
    inicio = hoy - timedelta(days=hoy.weekday())
    return inicio, inicio + timedelta(days=6)


def actualizar_vencidas():
    hoy = timezone.localdate()
    Cuota.objects.filter(estado='PENDIENTE', fecha_fin__lt=hoy).update(estado='VENCIDO')


@administrador_required
def lista_pagos(request):
    actualizar_vencidas()
    estado = request.GET.get('estado', '')
    cuotas = Cuota.objects.select_related('vivienda').all()
    if estado in {'PENDIENTE', 'PAGADO', 'VENCIDO'}:
        cuotas = cuotas.filter(estado=estado)
    inicio, fin = semana_actual()
    total_semana = Pago.objects.filter(fecha__date__range=(inicio, fin)).aggregate(total=Sum('monto'))['total'] or 0
    return render(request, 'pagos/lista.html', {
        'cuotas': cuotas[:300], 'estado': estado, 'total_semana': total_semana,
        'pendientes': Cuota.objects.filter(estado='PENDIENTE').count(),
        'vencidas': Cuota.objects.filter(estado='VENCIDO').count(),
    })


@administrador_required
def generar_cuotas(request):
    if request.method != 'POST':
        return redirect('lista_pagos')
    inicio, fin = semana_actual()
    creadas = 0
    for vivienda in Vivienda.objects.filter(activa=True):
        _, creada = Cuota.objects.get_or_create(
            vivienda=vivienda, fecha_inicio=inicio, fecha_fin=fin,
            defaults={'monto': vivienda.cuota_semanal},
        )
        creadas += int(creada)
    messages.success(request, f'Se generaron {creadas} cuotas para la semana {inicio:%d/%m} - {fin:%d/%m}.')
    return redirect('lista_pagos')


@administrador_required
def registrar_pago(request, cuota_id):
    cuota = get_object_or_404(Cuota.objects.select_related('vivienda'), pk=cuota_id)
    if hasattr(cuota, 'pago'):
        messages.info(request, 'Esta cuota ya tiene un pago registrado.')
        return redirect('lista_pagos')
    form = PagoForm(request.POST or None, request.FILES or None, cuota=cuota)
    if request.method == 'POST' and form.is_valid():
        pago = form.save(commit=False)
        pago.cuota = cuota
        pago.registrado_por = request.user
        pago.save()
        cuota.estado = 'PAGADO'
        cuota.save(update_fields=['estado'])
        enviar_confirmacion_pago(pago)
        messages.success(request, 'Pago registrado y confirmación enviada.')
        return redirect('lista_pagos')
    return render(request, 'pagos/registrar.html', {'form': form, 'cuota': cuota})


@administrador_required
def enviar_recordatorios(request):
    if request.method != 'POST':
        return redirect('lista_pagos')
    actualizar_vencidas()
    inicio, fin = semana_actual()
    cuotas = Cuota.objects.filter(fecha_inicio=inicio, fecha_fin=fin, estado__in=['PENDIENTE', 'VENCIDO']).select_related('vivienda')
    viviendas_notificadas = 0
    for cuota in cuotas:
        if enviar_recordatorio_cuota(cuota):
            viviendas_notificadas += 1
    messages.success(request, f'Recordatorios enviados a {viviendas_notificadas} viviendas con correo registrado.')
    return redirect('lista_pagos')
