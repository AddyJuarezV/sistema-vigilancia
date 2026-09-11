from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from accounts.decorators import administrador_required, personal_vigilancia_required
from .forms import ResidenteForm, ViviendaForm
from .models import Residente, Vivienda


@personal_vigilancia_required
def lista_viviendas(request):
    q = request.GET.get('q', '').strip()
    viviendas = Vivienda.objects.all()
    if q:
        viviendas = viviendas.filter(numero__icontains=q)
    return render(request, 'residentes/viviendas.html', {'viviendas': viviendas, 'q': q})


@administrador_required
def registrar_vivienda(request):
    form = ViviendaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Vivienda registrada correctamente.')
        return redirect('lista_viviendas')
    return render(request, 'residentes/vivienda_form.html', {'form': form, 'titulo': 'Registrar vivienda'})


@administrador_required
def editar_vivienda(request, pk):
    obj = get_object_or_404(Vivienda, pk=pk)
    form = ViviendaForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Vivienda actualizada.')
        return redirect('lista_viviendas')
    return render(request, 'residentes/vivienda_form.html', {'form': form, 'titulo': 'Editar vivienda'})


@administrador_required
def lista_residentes(request):
    q = request.GET.get('q', '').strip()
    residentes = Residente.objects.select_related('vivienda').all()
    if q:
        residentes = residentes.filter(nombre__icontains=q) | residentes.filter(apellido_paterno__icontains=q) | residentes.filter(vivienda__numero__icontains=q)
    return render(request, 'residentes/residentes.html', {'residentes': residentes, 'q': q})


@administrador_required
def registrar_residente(request):
    form = ResidenteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Residente registrado correctamente.')
        return redirect('lista_residentes')
    return render(request, 'residentes/residente_form.html', {'form': form, 'titulo': 'Registrar residente'})


@administrador_required
def editar_residente(request, pk):
    obj = get_object_or_404(Residente, pk=pk)
    form = ResidenteForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Residente actualizado.')
        return redirect('lista_residentes')
    return render(request, 'residentes/residente_form.html', {'form': form, 'titulo': 'Editar residente'})
