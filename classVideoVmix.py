#fichero = open('E:/ftp_enteltv_publicidad/GeneraListaReproduccionVMIX/lista.txt')
# python.exe -m pip install --upgrade pip
# instalar antes con: pip install requests
import requests
import time
import mutagen
import variables

class AppVideoVmix:
    
    def __init__(self, direccionVideo):

        self.direccion = direccionVideo
        self.nombre = self.extraeSoloNombre(direccionVideo)
        self.direccionVideo=self.corrigeDireccion(direccionVideo)
        self.nombreArchivo = self.extraeNombre(direccionVideo)
        self.urlTexto = "http://"+variables.ipAddress+":8088/api/?Function="
        self.duracionVideo = self.duracion(direccionVideo)
        self.duracionMinutos, self.duracionSegundos = divmod(self.duracionVideo, 60)
        self.duracionMinutos =  int(round(self.duracionMinutos,0))
        self.duracionSegundos = int(round(self.duracionSegundos,0))


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

    def extraeSoloNombre(self, direccion):
        # Extraemos nombre del archivp
        nombreArchivo = direccion.split("/")
        # Extraemos el nombre del archivo
        nombre = nombreArchivo[len(nombreArchivo)-1]
        return nombre

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
    
    # ENVIA EL VIDEO A REPRODUCIR                
    def duracion(self,dirArchivo):
        #print(f"Direccion del archivo para mutyage {dirArchivo}")
        #cancion_actual="E:/ftp_enteltv_publicidad/Publicidad/Largos/Instalaciones/VIDEO URUBICHA SANTA CRUZ.mp4"
        if len(dirArchivo) == 0:
            log=0
        else:
            audio = mutagen.File(dirArchivo)	
            log = audio.info.length
        #minutos, segundos = divmod(log, 60)
        return log
            
    # CARGAR VIDEO AL VMIX
    def cargarVideo(self):       
        # Formamos el comando para adicionar una entrada
        urlComando = self.urlTexto+"AddInput&Value=Video|" + self.direccionVideo
        #print(urlComando)
        r = requests.get(urlComando)
        r.close()

    # CARGAR VIDEO AL PREVIEW
    def cargarPreview(self):
        # Formamos el comando para enviar al preview
        urlComando = self.urlTexto+"PreviewInput&Input=" + self.nombreArchivo
        #print(urlTexto)
        r = requests.get(urlComando)
        r.close()

    # REPRODUCIR EL  VIDEO
    def reproducirVideo(self):
        # Formamos el comando para pasar del preview a output y reproducirlo
        urlComando = self.urlTexto+"QuickPlay&Input=" + self.nombreArchivo   
        #print(urlTexto)
        r = requests.get(urlComando)
        r.close()

    # ESPERAMOS QUE SE TERMINE DE REPRODUCIR EL VIDEO
    def esperarVideo(self):
        # Formamos el comando para esperar la reproduccion del video
        urlComando = self.urlTexto+"WaitForCompletion&Duration=600000&Input=" + self.nombreArchivo     
        #print(urlTexto)
        r = requests.get(urlComando)
        #print(r.content)
        r.close()

    # CERRAMOS EL VIDEO REPRODUCIDO
    def cerrarVideo(self):
        # Formamos el comando para cerrar el video
        urlComando = self.urlTexto+"RemoveInput&Input=" + self.nombreArchivo       
        #print(urlComando)
        r = requests.get(urlComando)
        r.close()
        