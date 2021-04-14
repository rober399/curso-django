from django.db import models

# Create your models here.



class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)   #FECHA AUTOMATICA
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:  #CLASE PARA ESPECIFICAR EL NOMBRE DEL SERVICIO EN LA BASE DE DATOS
        verbose_name='categoriaProd'
        verbose_name_plural='CategoriasProd'

    
    def __str__(self):    #METODO PARA RETORNAR EL TITULO DEL CATEGORIA
        return self.nombre




class Producto(models.Model):
    nombre=models.CharField(max_length=50) #CAMPO DE TEXTO
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE) #ESTABLECIENDO RELACION MUCHO A MUCHO CON CLASE CATEGORIA
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)    #IMAGEN
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)   #FECHA AUTOMATICA
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:  #CLASE PARA ESPECIFICAR EL NOMBRE DEL SERVICIO EN LA BASE DE DATOS
        verbose_name='producto'
        verbose_name_plural='productos'
    
    def __str__(self):    #METODO PARA RETORNAR EL TITULO DEL CATEGORIA
        return self.nombre

