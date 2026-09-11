from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def inicio(request):
    es_admin = request.user.groups.filter(name="Administrador").exists()
    es_guardia = request.user.groups.filter(name="Guardia").exists()

    return render(
        request,
        "dashboard/inicio.html",
        {
            "es_admin": es_admin,
            "es_guardia": es_guardia,
        }
    )