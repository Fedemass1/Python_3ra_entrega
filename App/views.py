from django.shortcuts import render, redirect
from App.models import Cliente, Producto, Venta
from App.forms import (ClienteForm, ProductoForm, VentaForm,
                       BuscarClienteForm)


def show_html(request):
    contexto = {

    }
    return render(request, 'index.html', contexto)


def mostrar_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {
        "clientes": clientes,
        "form": BuscarClienteForm,
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

            cliente_crear = Cliente(nombre=informacion["nombre"], dni=informacion["dni"],
                                    email=informacion["email"])
            cliente_crear.save()

            return redirect("/app/mostrar_clientes")

    return render(request, "App/agregar.html", contexto)


def agregar_producto_form(request):
    producto = ProductoForm
    contexto = {
        "form": producto
    }

    if request.method == "POST":
        producto = ProductoForm(request.POST)

        if producto.is_valid():
            informacion = producto.cleaned_data

            producto_crear = Producto(id_producto=informacion["id_producto"],
                                      nombre_producto=informacion["nombre_producto"],
                                      precio_venta=informacion["precio_venta"])

            producto_crear.save()
            return redirect("/app/mostrar_productos")

    return render(request, "App/agregar.html", contexto)


def mostrar_productos(request):
    productos = Producto.objects.all()
    contexto = {
        "productos": productos,
    }
    return render(request, "App/mostrar_productos.html", contexto)


def agregar_venta_form(request):
    venta = VentaForm
    contexto = {
        "form": venta
    }

    if request.method == "POST":
        venta = VentaForm(request.POST)

        if venta.is_valid():
            informacion = venta.cleaned_data

            venta_crear = Venta(dni=informacion["dni"], nombre_producto=informacion["nombre_producto"],
                                cantidad_vendida=informacion["cantidad_vendida"])

            venta_crear.save()
            return redirect("/app/mostrar_ventas")

    return render(request, "App/agregar.html", contexto)


def mostrar_ventas(request):
    ventas = Venta.objects.all()
    contexto = {
        "ventas": ventas,

    }
    return render(request, "App/mostrar_ventas.html", contexto)


def buscar_cliente(request):
    dni = request.GET["dni"]
    clientes = Cliente.objects.filter(dni__icontains=dni)

    contexto = {
        "clientes": clientes,
        "form": BuscarClienteForm,
    }
    return render(request, "App/mostrar_clientes.html", contexto)
