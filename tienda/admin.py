from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaProducto(admin.ModelAdmin):
    readonly_fields=('created', 'updated') #DEFINIENDO CAMPOS CREATED Y UPDATED COMO CAMPOS DE SOLO LECTURA


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')



admin.site.register(CategoriaProd, CategoriaProducto)
admin.site.register(Producto, ProductoAdmin)
