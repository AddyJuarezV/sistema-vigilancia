from django import forms
from .models import Residente, Vivienda


def estilizar(form):
    for field in form.fields.values():
        if isinstance(field.widget, forms.CheckboxInput):
            field.widget.attrs['class'] = 'form-check-input'
        else:
            field.widget.attrs['class'] = 'form-control'


class ViviendaForm(forms.ModelForm):
    class Meta:
        model = Vivienda
        fields = ['numero', 'calle', 'seccion', 'cuota_semanal', 'activa']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        estilizar(self)


class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ['vivienda', 'nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'correo', 'activo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        estilizar(self)
