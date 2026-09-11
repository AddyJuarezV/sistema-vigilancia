from django import forms
from .models import Paqueteria, Servicio


def estilos(form):
    for field in form.fields.values():
        field.widget.attrs['class'] = 'form-select' if isinstance(field.widget, forms.Select) else 'form-control'
        if isinstance(field.widget, forms.Textarea):
            field.widget.attrs['rows'] = 3


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['tipo', 'persona_empresa', 'vivienda', 'telefono', 'vehiculo', 'placas', 'observaciones']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs); estilos(self)


class PaqueteriaForm(forms.ModelForm):
    class Meta:
        model = Paqueteria
        fields = ['empresa', 'repartidor', 'vivienda', 'vehiculo', 'placas', 'observaciones']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs); estilos(self)
