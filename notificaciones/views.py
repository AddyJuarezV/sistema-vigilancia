from django.contrib import messages
from django.shortcuts import redirect, render
from accounts.decorators import personal_vigilancia_required
from .forms import AvisoForm
from .models import Aviso
from .services import distribuir_aviso


@personal_vigilancia_required
def lista_avisos(request):
    return render(request, 'notificaciones/avisos.html', {'avisos': Aviso.objects.all()[:200]})


@personal_vigilancia_required
def crear_aviso(request):
    form = AvisoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        aviso = form.save()
        enviados = distribuir_aviso(aviso)
        messages.success(request, f'Aviso registrado. Correos enviados: {enviados}.')
        return redirect('lista_avisos')
    return render(request, 'notificaciones/crear_aviso.html', {'form': form})


@personal_vigilancia_required
def aviso_basura(request):
    if request.method == 'POST':
        aviso = Aviso.objects.create(
            tipo='BASURA', titulo='Camión de basura dentro del fraccionamiento',
            mensaje='🚛 El camión recolector de basura acaba de ingresar al fraccionamiento. Favor de estar al pendiente.',
        )
        enviados = distribuir_aviso(aviso)
        messages.success(request, f'Ingreso del camión registrado. Correos enviados: {enviados}.')
    return redirect('lista_avisos')
