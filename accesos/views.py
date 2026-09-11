from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from accounts.decorators import personal_vigilancia_required
from .forms import AccesoVisitanteForm
from .models import AccesoVisitante


@personal_vigilancia_required
def activos(request):
    accesos = AccesoVisitante.objects.filter(salida__isnull=True).select_related('vivienda', 'guardia')
    return render(request, 'accesos/activos.html', {'accesos': accesos})


@personal_vigilancia_required
def registrar(request):
    form = AccesoVisitanteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        acceso = form.save(commit=False)
        acceso.guardia = request.user
        acceso.placas = acceso.placas.upper().strip()
        acceso.save()
        messages.success(request, 'Entrada de visitante registrada.')
        return redirect('accesos_activos')
    return render(request, 'accesos/registrar.html', {'form': form})


@personal_vigilancia_required
def salida(request, pk):
    acceso = get_object_or_404(AccesoVisitante, pk=pk, salida__isnull=True)
    if request.method == 'POST':
        acceso.salida = timezone.now()
        acceso.save(update_fields=['salida'])
        messages.success(request, 'Salida registrada correctamente.')
    return redirect('accesos_activos')


@personal_vigilancia_required
def historial(request):
    q = request.GET.get('q', '').strip()
    accesos = AccesoVisitante.objects.select_related('vivienda', 'guardia').all()
    if q:
        accesos = accesos.filter(Q(nombre__icontains=q) | Q(placas__icontains=q) | Q(vivienda__numero__icontains=q))
    return render(request, 'accesos/historial.html', {'accesos': accesos[:500], 'q': q})
