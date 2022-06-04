from django import forms
from apps.ejemplares.models import Ejemplar

class EjemplarForm(forms.ModelForm):
    class Meta:
        model=Ejemplar
        fields=[
            'libro',
            'localizacion',

            ]
        labels={
            'libro':'Ingrese Título del libro',
            'localizacion':'Ingrese Localización',
            
        }
        widgets={
            'libro':forms.Select(attrs={'class':'form-control'}),
            'localizacion':forms.TextInput(attrs={'class':'form-control'}),
            
        }