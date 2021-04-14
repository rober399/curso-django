from django import forms

#CREANDO FORMULARIO PARA CONTACTOS

class formularioContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)

    email=forms.EmailField(label="Email", required=True)

    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)








  