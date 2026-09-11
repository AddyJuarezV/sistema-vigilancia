from django import forms
from .models import Pago


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['residente', 'monto', 'metodo', 'referencia', 'comprobante']
        widgets = {
            'metodo': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, cuota=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.cuota = cuota
        for name, field in self.fields.items():
            if name != 'metodo':
                field.widget.attrs.setdefault('class', 'form-control')
        if cuota:
            self.fields['monto'].initial = cuota.monto
            self.fields['residente'].queryset = cuota.vivienda.residentes.filter(activo=True)

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('metodo') == 'TRANSFERENCIA' and not cleaned.get('referencia'):
            self.add_error('referencia', 'Captura una referencia para la transferencia.')
        return cleaned
