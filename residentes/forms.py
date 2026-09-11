from django import forms
from .models import Vivienda, Residente


class ViviendaForm(forms.ModelForm):
    class Meta:
        model = Vivienda
        fields = ["numero", "calle", "seccion", "activa"]


class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = [
            "vivienda",
            "nombre",
            "apellido_paterno",
            "apellido_materno",
            "telefono",
            "correo",
            "activo",
        ]