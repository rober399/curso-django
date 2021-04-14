from django.db import models
from django.utils.html import format_html  #FORMAT HTML SIRVE PARA PASAR TEXTO A FORMATO HTML

# Create your models here.
#MODELO PARA TABLA SERVICIOS
class Servicio(models.Model):
    titulo=models.CharField(max_length=50) #CAMPO DE TEXTO
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')    #IMAGEN
    created=models.DateTimeField(auto_now_add=True)   #FECHA AUTOMATICA
    updated=models.DateTimeField(auto_now_add=True) 


    class Meta:  #CLASE PARA ESPECIFICAR EL NOMBRE DEL SERVICIO EN LA BASE DE DATOS
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):    #METODO PARA RETORNAR EL TITULO DEL SERVICIO
        return self.titulo
