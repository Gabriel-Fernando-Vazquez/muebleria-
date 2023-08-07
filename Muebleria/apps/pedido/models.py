from django.db import models
from  apps.producto.models import Producto

# Create your models here.
class Pedido(models.Model):
    producto =  models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateTimeField('creado',auto_now_add=True)
    estado = models.BooleanField()
    anotaciones = models.TextField()