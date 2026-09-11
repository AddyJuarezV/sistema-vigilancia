from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Aviso
from .forms import AvisoForm


@login_required
def lista_avisos(request):
    avisos = Aviso.objects.all().order_by("-fecha")
    return render(
        request,
        "notificaciones/avisos.html",
        {"avisos": avisos}
    )


@login_required
def crear_aviso(request):
    if request.method == "POST":
        form = AvisoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_avisos")
    else:
        form = AvisoForm()

    return render(
        request,
        "notificaciones/crear_aviso.html",
        {"form": form}
    )