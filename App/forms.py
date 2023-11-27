from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=10)
    email = forms.EmailField()


class ProductoForm(forms.Form):
    id_producto = forms.CharField(max_length=10)
    nombre_producto = forms.CharField(max_length=50)
    precio_venta = forms.IntegerField()


class VentaForm(forms.Form):
    dni = forms.CharField(max_length=10)
    nombre_producto = forms.CharField(max_length=50)
    cantidad_vendida = forms.IntegerField()


class BuscarClienteForm(forms.Form):
    dni = forms.CharField()


