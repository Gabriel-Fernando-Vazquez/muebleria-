from django.db import models
from apps.producto.models import Categoria
from multiupload.fields import MultiImageField



class Muebles_personalizados(models.Model):
    nombre = models.CharField(max_length=100)
    desccripcion = models.TextField()
    imagene1 = models.ImageField(upload_to= 'muebles_personalizados')
    imagene2 = models.ImageField(upload_to= 'muebles_personalizados')
    imagene3 = models.ImageField(upload_to= 'muebles_personalizados')
    imagene4 = models.ImageField(upload_to= 'muebles_personalizados')
    imagene5 = models.ImageField(upload_to= 'muebles_personalizados')
    categoria = models.ForeignKey(Categoria ,on_delete = models.CASCADE) 
    materiales = models.TextField()
    dimensiones = models.CharField(max_length=200)
    creado = models.DateTimeField('creado',auto_now_add=True)
    modificado = models.DateTimeField('modificado',auto_now=True)

    
