from django.shortcuts import render
from tienda.models import Producto, CategoriaProd

# Create your views here.

def tienda(request):

    productos=Producto.objects.all()

    return render(request, "tienda/tienda.html", {"productos":productos}) #CARGANNDO PRODUCTOS DE VARIABLE PRODUCTOS


#def categoria(request, categoria_id):

    #categoria=CategoriaProd.objects.get(id=categoria_id)#FILTRANDO CATEGORIA

    #productos=Producto.objects.filter(categorias=categoria)

  
