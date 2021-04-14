from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage #SE USA PARA EL ENVIO DE CORREOS

# Create your views here.


def contacto(request):

    formulario_contacto=formularioContacto()  #INSTANCIANDO FORMULARIO

    if request.method=="POST":
        formulario_contacto=formularioContacto(data=request.POST)  #CARGANDAO INFORMACION INTRODUCIDA POR EL USUARIO
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre") #GUARDANDO VALOR EN VARIABLE
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            
            #CONFIGURACION PARA ENVIO DE CORREOS ELECTRONICOS POR PARTE DE USUARIOS
            email=EmailMessage("Mensaje desde App Django", 
            "El usuario con nombre: {} con la direccion: {}, escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
            "",["roberore99@gmail.com"], reply_to=[email])

            #EXCEPION EN CASO NO SE ENVIE EL CORREO
            try:
                email.send()

                return redirect("/contacto/?valido")   #REDIRECCIONANDO A PAGINA CONTACTO

            except:

                return redirect("/contacto/?novalido")


    return render(request, "contacto/contacto.html", {'miformulario': formulario_contacto})
