from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=10)
    email = forms.EmailField()
