import  mutagen
import time
def imprimir():
    print("ESTO  ES DE LA FUNCION")

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



