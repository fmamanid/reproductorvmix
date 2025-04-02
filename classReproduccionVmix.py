#instalar  pip install mutagen
#
from tkinter import *
import classVideoVmix
import classLogoVmix
import variables
import time
import funcion

class AppReproduccionVmix ():

    #######  Variables de la clase ######
    v_preview = ""
    v_out = ""
    v_del = ""
    nro_registro = 0
    lista_de_videos = []
    utlimo_registro = 0
    tiempo_duracion_video = 0
    tiempo_inicio = 0

    #########  Contructor  ###############
    def __init__(self, lista_de_videos, nro_registro):
        self.lista_de_videos = lista_de_videos
        self.nro_registro = nro_registro
        self.utlimo_registro = len(lista_de_videos) -1



        
    def imprimir_lista(self):
        for fila in self.lista_de_videos:
            print(fila[4])



    def reproducir_video(self):
        print(f"####   {self.nro_registro}   ####")
        if self.nro_registro == 0:
            self.v_preview = self.lista_de_videos[self.nro_registro + 1][4] #   get_ubicacion_reg(nro_registro+1)
            self.v_out = self.lista_de_videos[self.nro_registro][4]  # get_ubicacion_reg(nro_registro)
            self.v_del = ""
            self.emitir_video(1)

        elif self.nro_registro == self.utlimo_registro:
            self.v_preview = ""
            self.v_out = self.lista_de_videos[self.nro_registro][4] #get_ubicacion_reg(nro_registro)
            self.v_del = self.lista_de_videos[self.nro_registro - 1][4] #get_ubicacion_reg(nro_registro-1)
            self.emitir_video(3)  
            
        elif self.nro_registro == self.utlimo_registro + 1:
            self.v_preview = ""
            self.v_out = ""
            self.v_del = self.lista_de_videos[self.nro_registro - 1][4] # get_ubicacion_reg(nro_registro-1)
            self.emitir_video(4)    
                
        elif self.nro_registro > self.utlimo_registro + 1:
            print(f"####SALIENDO   {self.nro_registro}   SALIENDO####3")
            
        else:
            self.v_preview = self.lista_de_videos[self.nro_registro + 1][4]  #get_ubicacion_reg(nro_registro+1)
            self.v_out = self.lista_de_videos[self.nro_registro][4]  # get_ubicacion_reg(nro_registro)
            self.v_del = self.lista_de_videos[self.nro_registro - 1][4]  #get_ubicacion_reg(nro_registro-1)
            self.emitir_video(2)

        print(self.v_preview)
        print(self.v_out)
        print(self.v_del)

    def emitir_video(self, opcion):

        ####  INCIALIZAMOS LOS OBJETOS VMIX ###########
        videoPreviewVmix = classVideoVmix.AppVideoVmix(self.v_preview)
        videoOutVmix = classVideoVmix.AppVideoVmix(self.v_out )
        videoDelVmix = classVideoVmix.AppVideoVmix(self.v_del )
        miLogo = classLogoVmix.AppLogoVmix(variables.direccionLogo)
        if opcion == 1:
            videoOutVmix.cargarVideo()
            time.sleep(1)
            videoPreviewVmix.cargarVideo()
            time.sleep(1)
            videoOutVmix.reproducirVideo()
            
            self.tiempo_duracion_video = funcion.duracion_video(self.v_out)

            self.tiempo_inicio = time.time()

            miLogo.reproduceLogo(videoOutVmix.nombreArchivo)
            time.sleep(1)
            videoPreviewVmix.cargarPreview()
            

        elif opcion == 2:
            videoDelVmix.esperarVideo()
            videoOutVmix.reproducirVideo()
            
            self.tiempo_duracion_video = funcion.duracion_video(self.v_out)

            self.tiempo_inicio = time.time()

            print(f"video reproducido: {videoOutVmix.direccionVideo} el criterio es {variables.criterioLogo}  la direccion del logo es: {variables.direccionLogo}")
            miLogo.reproduceLogo(videoOutVmix.direccionVideo)
            time.sleep(1)
            videoDelVmix.cerrarVideo()
            time.sleep(1)
            videoPreviewVmix.cargarVideo()
            time.sleep(1)
            videoPreviewVmix.cargarPreview()
            #self.tiempo_del_video = funciones.duracion_video(v_Out)+15

        elif opcion == 3:
            videoDelVmix.esperarVideo()
            videoOutVmix.reproducirVideo()
            
            self.tiempo_duracion_video = funcion.duracion_video(self.v_out)

            self.tiempo_inicio = time.time()
            
            miLogo.reproduceLogo(videoOutVmix.nombreArchivo)
            time.sleep(1)
            videoDelVmix.cerrarVideo()
            #tiempo_duracion_video = funcion.duracion_video(self.v_Out)+5

        elif opcion == 4:
            videoDelVmix.esperarVideo()
            time.sleep(1)
            videoDelVmix.cerrarVideo()
            
