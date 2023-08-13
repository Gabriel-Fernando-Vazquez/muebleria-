from django.db import models
from multiupload.fields import MultiImageField
from apps.producto.models import  Categoria

class Diseño_interior(models.Model):
    nombre = models.CharField(max_length=100)
    imagene1 = models.ImageField(upload_to='interiores')
    imagene2 = models.ImageField(upload_to='interiores')
    imagene3 = models.ImageField(upload_to='interiores')
    imagene4 = models.ImageField(upload_to='interiores')
    imagene5 = models.ImageField(upload_to='interiores')
    imagene6 = models.ImageField(upload_to='interiores')
    imagene7 = models.ImageField(upload_to='interiores')
    imagene8 = models.ImageField(upload_to='interiores')
    imagene9 = models.ImageField(upload_to='interiores')
    imagene10 = models.ImageField(upload_to='interiores')
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    materiales = models.TextField()
    dimensiones = models.CharField(max_length=100)
    creado = models.DateTimeField('creado',auto_now_add=True)
    modificado = models.DateTimeField('modificado',auto_now=True)



