import tkinter as tk
import mutagen
import time


ventana = tk.Tk()
ventana.title("temporizador videos")
ventana.geometry("260x160+900+100")



#########funciones #########3

inicio = 0
duracion = 0
tarea = None
tamCancion = 0
def iniciar():
    global inicio
    global duracion
    global tarea
    global tamCancion

    cancion_actual = "D:/ftp_enteltv_publicidad/Publicidad/Cortos/Spots/Spot 2 Bolivianos.mp4"
    audio = mutagen.File(cancion_actual)	
    log = audio.info.length
    tamCancion = log
    minutos, segundos = divmod(log, 60)
    print(f" {log} minutos: {minutos}  y segundos: {segundos}")
    duracion = 0
    inicio = time.time()
    print(inicio)
    etiqueta.after(300,actualizarRotulo)

def actualizarRotulo():
    global tarea
    global tamCancion
    global duracion

    titulo.set(int(round(duracion,0)))
    tarea = etiqueta.after(300, actualizarRotulo)
    duracion =   time.time() - inicio 

    if duracion > tamCancion - 1:
        etiqueta.after_cancel(tarea)
    print(f" cancion: {tamCancion}  duracion: {duracion}")

##### greacion de wifget ###########
titulo = tk.StringVar()
titulo.set(f"0")
etiqueta = tk.Label(ventana,
                    textvariable=titulo,
                    width=10,
                    bg="white",
                    font="consolas 20 bold",
                    
                    )
etiqueta.pack(padx=10, pady=10)
btnIniciar = tk.Button(text="Iniciar",
                       command=iniciar)
btnIniciar.pack()

ventana.mainloop()