from django.shortcuts import render, redirect
from apps.ejemplares.models import Ejemplar
from apps.ejemplares.formEjem import EjemplarForm

# Create your views here.

def listEjemplares(request):
    ejemplares=Ejemplar.objects.all().order_by('id')
    contexto={'ejemplares':ejemplares}
    return render(request, 'listEjemplares.html', contexto)

def inicio(request):
    contexto={'inicio':inicio}
    return render(request, 'inicio.html', contexto)

def ejemplarCreate(request):
    if request.method=='POST':
        form=EjemplarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ejemplares:listEjemplares')
    else:
        form=EjemplarForm()
        return render(request, 'ejem_form.html', {'form':form})
    