from django.core.mail import send_mail
from residentes.models import Residente


def correos_vivienda(vivienda):
    return list(
        Residente.objects.filter(vivienda=vivienda, activo=True)
        .exclude(correo='')
        .values_list('correo', flat=True)
    )


def enviar_confirmacion_pago(pago):
    destinatarios = correos_vivienda(pago.cuota.vivienda)
    if not destinatarios:
        return 0
    asunto = 'Pago de vigilancia recibido correctamente'
    mensaje = (
        f'Hola.\n\nEl pago de vigilancia de la vivienda {pago.cuota.vivienda.numero} '
        f'correspondiente del {pago.cuota.fecha_inicio:%d/%m/%Y} al {pago.cuota.fecha_fin:%d/%m/%Y} '
        f'por ${pago.monto} fue registrado correctamente.\n\nGracias.'
    )
    return send_mail(asunto, mensaje, None, destinatarios, fail_silently=True)


def enviar_recordatorio_cuota(cuota):
    destinatarios = correos_vivienda(cuota.vivienda)
    if not destinatarios:
        return 0
    asunto = 'Recordatorio de pago de vigilancia'
    mensaje = (
        f'Le recordamos que la vivienda {cuota.vivienda.numero} tiene pendiente la cuota de vigilancia '
        f'del {cuota.fecha_inicio:%d/%m/%Y} al {cuota.fecha_fin:%d/%m/%Y} por ${cuota.monto}.\n\n'
        'Favor de pasar a realizar el pago o enviar la transferencia a administración.'
    )
    return send_mail(asunto, mensaje, None, destinatarios, fail_silently=True)
