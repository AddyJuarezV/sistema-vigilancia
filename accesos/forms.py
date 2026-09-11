from django import forms
from .models import AccesoVisitante


class AccesoVisitanteForm(forms.ModelForm):
    class Meta:
        model = AccesoVisitante
        fields = ['nombre', 'vivienda', 'motivo', 'tipo_identificacion', 'identificacion_verificada', 'vehiculo', 'color', 'placas', 'observaciones']
        widgets = {'observaciones': forms.Textarea(attrs={'rows': 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
