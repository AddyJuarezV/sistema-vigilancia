from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from accounts.decorators import personal_vigilancia_required
from .forms import PaqueteriaForm, ServicioForm
from .models import Paqueteria, Servicio


@personal_vigilancia_required
def panel(request):
    servicios = Servicio.objects.filter(salida__isnull=True).select_related('vivienda', 'guardia')
    paquetes = Paqueteria.objects.filter(salida__isnull=True).select_related('vivienda', 'guardia')
    return render(request, 'servicios/panel.html', {'servicios': servicios, 'paquetes': paquetes})


@personal_vigilancia_required
def nuevo_servicio(request):
    form = ServicioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        obj = form.save(commit=False); obj.guardia = request.user; obj.placas = obj.placas.upper().strip(); obj.save()
        messages.success(request, 'Servicio registrado.')
        return redirect('panel_servicios')
    return render(request, 'servicios/form.html', {'form': form, 'titulo': 'Registrar servicio'})


@personal_vigilancia_required
def nueva_paqueteria(request):
    form = PaqueteriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        obj = form.save(commit=False); obj.guardia = request.user; obj.placas = obj.placas.upper().strip(); obj.save()
        messages.success(request, 'Paquetería registrada.')
        return redirect('panel_servicios')
    return render(request, 'servicios/form.html', {'form': form, 'titulo': 'Registrar paquetería'})


@personal_vigilancia_required
def salida_servicio(request, pk):
    obj = get_object_or_404(Servicio, pk=pk, salida__isnull=True)
    if request.method == 'POST':
        obj.salida = timezone.now(); obj.save(update_fields=['salida']); messages.success(request, 'Salida del servicio registrada.')
    return redirect('panel_servicios')


@personal_vigilancia_required
def salida_paqueteria(request, pk):
    obj = get_object_or_404(Paqueteria, pk=pk, salida__isnull=True)
    if request.method == 'POST':
        obj.salida = timezone.now(); obj.save(update_fields=['salida']); messages.success(request, 'Salida de paquetería registrada.')
    return redirect('panel_servicios')


@personal_vigilancia_required
def historial(request):
    return render(request, 'servicios/historial.html', {
        'servicios': Servicio.objects.select_related('vivienda', 'guardia').all()[:300],
        'paquetes': Paqueteria.objects.select_related('vivienda', 'guardia').all()[:300],
    })
