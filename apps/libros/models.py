from django.db import models

# Create your models here.


class Libro(models.Model):
    título = models.CharField(verbose_name="Título", max_length=120)
    núm_pag=models.SmallIntegerField(verbose_name="Número de Página")
    editorial=models.CharField(verbose_name="Editorial",max_length=50)
    isbn=models.CharField(verbose_name="ISBN", max_length=50) 
    autor=models.CharField(verbose_name="Autor", max_length=50)
    def __str__(self):
        return self.título