from django import forms
from .models import Aviso

class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ['tipo', 'titulo', 'mensaje', 'activo']
        widgets = {'mensaje': forms.Textarea(attrs={'rows': 4})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput): field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select): field.widget.attrs['class'] = 'form-select'
            else: field.widget.attrs['class'] = 'form-control'
