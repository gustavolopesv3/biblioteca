from django import forms

from cadastro.models import Socio


class FormSocio(forms.ModelForm):
    class Meta:
        model = Socio
        fields = "__all__"
