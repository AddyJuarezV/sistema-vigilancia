from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils import timezone

from residentes.models import Residente
from .models import Aviso, Notificacion
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
            aviso = form.save()

            residentes = Residente.objects.filter(
                activo=True
            ).exclude(
                correo=""
            )

            for residente in residentes:
                enviada = False
                fecha_envio = None

                try:
                    send_mail(
                        aviso.titulo,
                        aviso.mensaje,
                        None,
                        [residente.correo],
                        fail_silently=False,
                    )

                    enviada = True
                    fecha_envio = timezone.now()

                except Exception:
                    enviada = False

                Notificacion.objects.create(
                    residente=residente,
                    aviso=aviso,
                    enviada=enviada,
                    fecha_envio=fecha_envio,
                )

            return redirect("lista_avisos")

    else:
        form = AvisoForm()

    return render(
        request,
        "notificaciones/crear_aviso.html",
        {"form": form}
    )