from django.shortcuts import render
# Establecer comunicación con el modelo
from .models import Service

# Create your views here.
def services(request):
    # Obtener datos
    services = Service.objects.all()
    # Diccionario
    return render(request, 'services/services.html', {'listServices':services})

