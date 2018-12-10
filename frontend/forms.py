from django import forms


class BuscarForm(forms.Form):
    buscar = forms.CharField(max_length=50)