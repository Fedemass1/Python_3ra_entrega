from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)


class Producto(models.Model):
    id_producto = models.CharField(max_length=10, unique=True)
    nombre_producto = models.CharField(max_length=50)
    precio_venta = models.IntegerField()


class Venta(models.Model):
    dni = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=50)
    cantidad_vendida = models.IntegerField()

