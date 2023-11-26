from django.urls import path
from App.views import show_html, agregar_cliente_form, mostrar_clientes

urlpatterns = [
    path('show/', show_html),
    path('clientes/', agregar_cliente_form),
    path('mostrar_clientes/', mostrar_clientes),

]
