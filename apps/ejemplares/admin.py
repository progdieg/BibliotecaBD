from django.contrib import admin
from apps.ejemplares.models import Ejemplar, Prestamo

# Register your models here.


class EjemplarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Prestamo)