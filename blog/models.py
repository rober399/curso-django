from django.db import models
from django.contrib.auth.models import User    #IMPORTANDO USUARIOS

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50) #CAMPO DE TEXTO
    created=models.DateTimeField(auto_now_add=True)   
    updated=models.DateTimeField(auto_now_add=True) 


    class Meta:  #CLASE PARA ESPECIFICAR EL NOMBRE DEL SERVICIO EN LA BASE DE DATOS
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):    #METODO PARA RETORNAR EL TITULO DEL CATEGORIA
        return self.nombre




class Post(models.Model):
    titulo=models.CharField(max_length=50) #CAMPO DE TEXTO
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)    #IMAGEN
    autor=models.ForeignKey(User, on_delete=models.CASCADE)      #RELACION FORANEA Y DELETE EN CASCADA DE POST SEGUN AUTOR
    categorias=models.ManyToManyField(Categoria) #ESTABLECIENDO RELACION MUCHO A MUCHO CON CLASE CATEGORIA
    created=models.DateTimeField(auto_now_add=True)   #FECHA AUTOMATICA
    updated=models.DateTimeField(auto_now_add=True) 


    class Meta:  #CLASE PARA ESPECIFICAR EL NOMBRE DEL SERVICIO EN LA BASE DE DATOS
        verbose_name='post'
        verbose_name_plural='post'
    
    def __str__(self):    #METODO PARA RETORNAR EL TITULO DEL SERVICIO
        return self.titulo
