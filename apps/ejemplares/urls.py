from django.urls import path
from apps.ejemplares.views import listEjemplares, inicio
from . import views

app_name = 'ejemplares'
urlpatterns = [
    path('', listEjemplares, name='listEjemplares'),
    path('', views.inicio, name='inicio'),
]

