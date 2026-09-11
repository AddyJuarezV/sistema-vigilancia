from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Vivienda, Residente
from .forms import ViviendaForm, ResidenteForm


@login_required
def lista_viviendas(request):
    viviendas = Vivienda.objects.all().order_by("numero")
    return render(
        request,
        "residentes/viviendas.html",
        {"viviendas": viviendas}
    )


@login_required
def lista_residentes(request):
    residentes = Residente.objects.select_related("vivienda").all()
    return render(
        request,
        "residentes/residentes.html",
        {"residentes": residentes}
    )


@login_required
def registrar_vivienda(request):
    if request.method == "POST":
        form = ViviendaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_viviendas")
    else:
        form = ViviendaForm()

    return render(
        request,
        "residentes/registrar_vivienda.html",
        {"form": form}
    )


@login_required
def registrar_residente(request):
    if request.method == "POST":
        form = ResidenteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_residentes")
    else:
        form = ResidenteForm()

    return render(
        request,
        "residentes/registrar_residente.html",
        {"form": form}
    )