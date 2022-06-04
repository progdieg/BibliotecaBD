from django.db import models
from django.contrib.auth.models import User
from apps.libros.models import Libro

# Create your models here.

class Ejemplar(models.Model):
    libro= models.ForeignKey(Libro, verbose_name="Título del libro", on_delete=models.CASCADE)
    localizacion=models.CharField(verbose_name="Localización",max_length=60)
    usuario=models.ManyToManyField(User, through="Prestamo")
    def __str__(self):
        return self.libro.título
    
    
class Prestamo(models.Model):
    usuario=models.ForeignKey(User, verbose_name="Usuario", blank=True, null=True, on_delete=models.CASCADE)
    ejemplar=models.ForeignKey(Ejemplar, verbose_name="Ejemplar", blank=True, null=True, on_delete=models.CASCADE)
    fecha_dev=models.DateField(verbose_name="Fecha de Devolución")
    fecha_pres=models.DateField(verbose_name="Fecha de Préstamo")
    def __str__(self):
        return self.usuario.username
