from django.shortcuts import render, redirect
from App.models import Cliente, Producto, Venta
from App.forms import ClienteForm


def show_html(request):
    contexto = {

    }
    return render(request, 'index.html', contexto)


def mostrar_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {
        "clientes": clientes,
    }

    return render(request, "App/mostrar_clientes.html", contexto)


def agregar_cliente_form(request):
    cliente = ClienteForm
    contexto = {
        "form": cliente
    }

    if request.method == "POST":
        cliente = ClienteForm(request.POST)

        if cliente.is_valid():
            informacion = cliente.cleaned_data

            cliente_crear = Cliente(nombre=informacion["nombre"], dni=informacion["dni"], email=informacion["email"])
            cliente_crear.save()
            return redirect("/app/mostrar_clientes")

    return render(request, "App/agregar_cliente.html", contexto)
