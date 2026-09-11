from django.core.mail import send_mail
from django.utils import timezone
from residentes.models import Residente
from .models import Notificacion


def distribuir_aviso(aviso):
    enviados = 0
    residentes = Residente.objects.filter(activo=True).exclude(correo='').select_related('vivienda')
    for residente in residentes:
        ok = False
        fecha = None
        try:
            ok = bool(send_mail(aviso.titulo, aviso.mensaje, None, [residente.correo], fail_silently=False))
            if ok:
                fecha = timezone.now(); enviados += 1
        except Exception:
            ok = False
        Notificacion.objects.create(residente=residente, aviso=aviso, enviada=ok, fecha_envio=fecha)
    return enviados
