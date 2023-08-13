from django.db import models





class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to= 'categoria')

class Sub_categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to= 'sub_categoria')

class Producto_venta_masiva(models.Model):
    nombre = models.CharField(max_length= 100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagene1 : models.ImageField(upload_to= 'productos')
    imagene2 : models.ImageField(upload_to= 'productos')
    imagene3 : models.ImageField(upload_to= 'productos')
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    sub_categoria = models.ForeignKey(Sub_categoria, on_delete= models.CASCADE)
    material = models.CharField(max_length=100)
    dimensiones = models.CharField(max_length=100)
    disponibilidad = models.IntegerField()
    creado = models.DateTimeField('creado',auto_now_add=True)
    modificado = models.DateTimeField('modificado',auto_now=True)






