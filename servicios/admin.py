from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):   #CLASE PARA AGREGAR UPDATE Y CREATED EN EL PANEL DE ADMINISTRACION
    readonly_fields=('created', 'updated')

admin.site.register(Servicio, ServiciosAdmin)