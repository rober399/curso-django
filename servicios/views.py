from django.shortcuts import render

from servicios.models import Servicio


# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()   #importando todos los servicios construidos

    return render(request, "servicios/servicios.html", {"servicios":servicios}) #Cargando servicios incluidos