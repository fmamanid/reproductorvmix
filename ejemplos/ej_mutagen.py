from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
import mutagen

cancion_actual="E:/ftp_enteltv_publicidad/Publicidad/Largos/Instalaciones/VIDEO URUBICHA SANTA CRUZ.mp4"
audio = mutagen.File(cancion_actual)	
log = audio.info.length
minutos, segundos = divmod(log, 60)

print(f"el video tiene {minutos} [min] con {segundos} [s]")
