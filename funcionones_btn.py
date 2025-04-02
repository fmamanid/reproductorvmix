from tkinter import filedialog , messagebox
import mutagen
import classVideoVmix

def nombre_video(video_actual):
    nombre_cancion = video_actual.split('/')
    nombre_cancion = nombre_cancion[-1] 
    return  nombre_cancion    

def duracion_video(ruta_video):
    #cancion_actual="E:/ftp_enteltv_publicidad/Publicidad/Largos/Instalaciones/VIDEO URUBICHA SANTA CRUZ.mp4"
    audio = mutagen.File(ruta_video)	
    log = audio.info.length
    #minutos, segundos = divmod(log, 60)

    #print(f"el video tiene {minutos} [min] con {segundos} [s]")
    return log

def Agregar():
    #self.direccion = filedialog.askopenfilename(initialdir='D:/cursos/aplicacionesepython/prueba',
    #                                  title='Abrir archivo',
    #                                  filetypes=(('Archivos de video','*.m3u'),('Todos los archivos','*.*'))
    #                                  )
    #self.lblSeleccionado.configure(text=self.direccion)
    #if len(self.direccion)==0:
    #    messagebox.showwarning("Abrir","Debe seleccionar un archivo")
    direcion = filedialog.askopenfilenames(initialdir ='/', 
                                            title='Escoger archivos de video', 
                                        filetype=(('m3u files', '*.m3u*'), ('mp4 files', '*.mp4*')))
    n = len(direcion)
    linea=""

    dir_videos = ""
    if n == 1:
        linea = direcion[0]
        if linea.find(".m3u") > 0:
            print(f"es un archivo es {nombre_video(linea)}")
            f = open(linea, "r")
            dir_videos = f

        elif linea.find(".mp4") > 0:
            print(f"el archivo es {nombre_video(linea)}")
            dir_videos= direcion
        else:
            print("el archivo no tiene el formato valido")
    elif n == 0:
        messagebox.showwarning("Abrir","Debe elegir al menos un archivo")
        return
    else:
        print(f"son {n} archivo .mp4")
        dir_videos= direcion

    #lista = direcion
    #print(f"el archvivo contiene {n} archivos y el tipo de archivo es {type(direcion)}")
    i=0
    lista_videos = []
    
    for linea in dir_videos:
        i+=1
        aux = linea.replace("\n","")
        #print(aux)
        lista_videos.append(classVideoVmix.AppVideoVmix(aux))
        #direccion = aux
        #nombre = nombre_video(aux)
        #cargar_datos(i,nombre,direccion)
    #print(direcion)

    return lista_videos


