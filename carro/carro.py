class Carro:
    def __init__(self, request):
        self.request=request #ALMACENANDO PETICION PARA ENTRAR AL CARRITO EN REQUEST
        self.session=request.session  #INICIANDO SESION
        carro=self.session.get("carro")
        if  not carro:   #SI NO HAY CARRO EN LA SESION
            carro=self.session["carro"]={} #CREA CARRO CON UN DICCIONARIO VACIO
        else:   #SI HAY CARRO EN LA SESION
            self.carro=carro  #IGUALANDO CARRO AL CARRO QUE YA HABIA EN LA SESION

    
    def agregar(self, producto): #FUNCION PARA AGREGAR PRODUCTOS AL CARRO
        if(str(producto.id) not in self.carro.keys()):  #SI NO ENCUENTRA EL ID DEL PRODUCTO EN EL CARRO
            self.carro[producto.id]={     #AGREGA PRODUCTO AL CARRO DICCIONARIO CLAVE-VALOR
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,  #CANTIDAD DE PRODUCTOS EN PRINCIPIO 1
                "imagen":producto.imagen.url
            }

        else:
            for key, value in self.carro.items(): #POR CADA CLAVE VALOR EN EL CARRO
                if key==str(producto.id):  #COMPROBANDO SI CLAVE ES IGUAL A ALGUN ID DE UN PRODUCTO EN EL CARRO
                    value["cantidad"]=value["cantidad"]+1 #LE SUMA UN VALOR MAS A LA CANTIDAD DE PRODUTOS
                    break #CERRANDO FOR EN CASO YA ENCUENTRE EL PRODUCTO
        self.guardar_carro()

    
    def guardar_carro(self):   #FUNCION PARA ACTUALIZAR SESION
        self.session["carro"]=self.carro
        self.session.modified=True

    
    def eliminar(self, producto):  #FUNCION PARA ELIMINAR UN PRODUCTO DEL CARRO
        producto.id=str(producto.id)   #OBTENIENDO ID DE PRODUCTO
        if producto.id in self.carro:   #COMPROBANDO QUE ESE ID DE PRODUCTO ESTE EN EL CARRO
            del self.carro[producto.id]      #QUITANDO PRODUCTO  DEL CARRO
            self.guardar_carro()  #ACTUALIZANDO CARRO

    
    def restar_producto(self, producto):  #FUNCION PARA RESTAR UNIDADES AL PRODUCTO AGREGADO AL CARRO
        for key, value in self.carro.items():
                if key==str(producto.id): 
                    value["cantidad"]=value["cantidad"]-1 
                    if value["cantidad"]<1: #SI LA CANTIDAD DE PRODUCTOS ES MENOR QUE 1
                        self.eliminar(producto) #LLAMA A FUNCION ELIMINAR PARA BORRAR PRODUCTO DEL CARRO
                    break 
        self.guardar_carro()#ACTUALIZANDO CARRO


    
    def limpiar_carro(self):
        self.session["carro"]={}  #CONSTRUTE DICCIONARIO VACIO
        self.session.modified=True






    





