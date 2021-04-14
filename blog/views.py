from django.shortcuts import render

from blog.models import Post, Categoria


# Create your views here.


def blog(request):
    
    posts=Post.objects.all() 

    return render(request, "blog/blog.html", {"posts":posts}) #Cargando Post incluidos de variable post


def categoria(request, categoria_id):  # pasadno id_categoria por parametros

    categoria=Categoria.objects.get(id=categoria_id) #Filtrando categoria

    posts=Post.objects.filter(categorias=categoria)

    return render(request, "blog/categorias.html", {'categoria':categoria, "posts":posts})

