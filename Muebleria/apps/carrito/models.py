from django.db import models
from django.contrib.auth.models import User
from apps.producto.models import Producto_venta_masiva
# Create your models here.

class Carrito(models.Model):
    cliente = models.ForeignKey(User, on_delete = models.CASCADE)
    productos = models.ManyToManyField(Producto_venta_masiva)
    creacion = models.DateTimeField('creado',auto_now_add=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)


    