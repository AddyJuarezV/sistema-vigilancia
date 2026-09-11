from django import forms
from .models import Aviso


class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ["tipo", "titulo", "mensaje", "activo"]