from django.urls import path
from App.views import (show_html, agregar_cliente_form, mostrar_clientes,
                       agregar_producto_form, mostrar_productos, agregar_venta_form,
                       mostrar_ventas, buscar_cliente)

urlpatterns = [
    path('show/', show_html),
    path('clientes/', agregar_cliente_form),
    path('mostrar_clientes/', mostrar_clientes),
    path('productos/', agregar_producto_form),
    path('mostrar_productos/', mostrar_productos),
    path('ventas/', agregar_venta_form),
    path('mostrar_ventas/', mostrar_ventas),
    path('buscar_cliente/', buscar_cliente),


]
