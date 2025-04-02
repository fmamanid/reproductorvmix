#instalar  pip install mutagen
#
from tkinter import *
import requests
import variables
#from tkinter import ttk
#from tkinter import messagebox
#from tkinter import filedialog
#from classVmix import *
#import mutagen

class AppLogoVmix ():

    direccionArchivo=""
    def __init__(self, direccionArchivo):
        self.urlTexto = "http://"+variables.ipAddress+":8088/api/?Function="
        self.direccionLogo=self.corrigeDireccion(direccionArchivo)
        self.nombreLogo = self.extraeNombre(direccionArchivo)
        self.criterioLogo = variables.criterioLogo

    ############################ Funciones###############################
    # CORRIGE LA DIRECCION 
    def corrigeDireccion(self, miDireccion):
        # Variable que contiene la direccion del archivo
        direccionArchivo = miDireccion
        # Reemplazamos los espacios en blanco con el caracter %20
        direccionArchivoCorregido = direccionArchivo.replace(' ','%20')
        direccionArchivoCorregido = direccionArchivoCorregido.replace("\n","")
        # Retornamos la direccion del archivo corregido
        return direccionArchivoCorregido
    #
    # EXTRAE EL NOMBRE DE LA DIRECCION DEL ARCHIVO
    def extraeNombre(self, direccion):
        # Extraemos nombre del archivp
        nombreArchivo = direccion.split("/")
        # Extraemos el nombre del archivo
        nombre = nombreArchivo[len(nombreArchivo)-1]
        # Reemplazamos los espacios en blanco con el caracter %20
        nombreCorregido = nombre.replace(' ','%20')
        nombreCorregido = nombreCorregido.replace("\n","")
        # Retornamos el nombre corregido
        return nombreCorregido
    
    # INSERTAR LOGO
    def insertarLogo(self):
        # Formamos el comando para adicionar una entrada
        urlComando = self.urlTexto+"OverlayInput4In&Input=" + self.nombreLogo 
        #print(urlComando)
        r = requests.get(urlComando)
        r.close()

    # QUITAR LOGO
    def quitarLogo(self):
        # Formamos el comando para adicionar una entrada
        urlComando = self.urlTexto+"OverlayInput4Off&Input=" + self.nombreLogo 
        r = requests.get(urlComando)
        r.close()   

    # ENVIA EL VIDEO A REPRODUCIR
    def reproduceLogo(self, nombreVideo):
        numero = nombreVideo.find(variables.criterioLogo)

        #print(f"Direccion del video: {nombreVideo} y el numero es: {numero}")

        self.cerrarOverlays()
        # Si Tenemos condicion de logo
        if  (numero >= 0) :
            self.insertarLogo()
        # No tenemos condicion de logo
        else:
            # Si el logo esta habilitado, lo deshabilitamos
            self.quitarLogo()
            
    # CERRAR TODOS LOS LOGOS
    def cerrarOverlays(self):
        # Formamos el comando
        urlComando = self.urlTexto+"OverlayInputAllOff"
        # enviamos el comando
        r = requests.get(urlComando)
        r.close()
        
    # CARGAR LOGO
    def cargarLogo(self):       
        # Formamos el comando para adicionar una entrada
        urlComando = self.urlTexto+"AddInput&Value=Title|" + self.direccionLogo
        #print(urlComando)
        r = requests.get(urlComando)
        r.close()