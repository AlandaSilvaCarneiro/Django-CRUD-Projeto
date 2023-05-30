from django import forms
from cliente import models



class ClienteForma(forms.ModelForm):
    class Meta:
        model =models.Cliente
        filds = "__all__"