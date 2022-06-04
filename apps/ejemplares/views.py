from django.shortcuts import render
from apps.ejemplares.models import Ejemplar

# Create your views here.

def listEjemplares(request):
    ejemplares=Ejemplar.objects.all().order_by('id')
    contexto={'ejemplares':ejemplares}
    return render(request, 'listEjemplares.html', contexto)

def inicio(request):
    contexto={'inicio':inicio}
    return render(request, 'inicio.html', contexto)