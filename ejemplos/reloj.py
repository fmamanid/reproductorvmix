import tkinter as tk
from tkinter import ttk
import time




##### VENTANA PRINCIPAL #####


ventana = tk.Tk()
ventana.title("Reloj digital")
ventana.geometry("260x160+900+100")






##### FUNCIONES RELOJ #####




def actualizar_hora():
    hora.set(time.strftime("%H:%M:%S"))
    rotulo_hora.after(500, actualizar_hora)
    rotulo_hora.focus()




def actualizar_fecha():
    fecha.set(time.strftime("%d / %m / %Y"))
    rotulo_fecha.after(500, actualizar_fecha)






##### FUNCIONES CRONOMETRO #####


horas, minutos, segundos = 0, 0, 0
tarea = None




def iniciar_cronometro():


    global horas, minutos, segundos
    global tarea


    tiempo.set(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1
    tarea = rotulo_cronometro.after(1000, iniciar_cronometro)


    rotulo_cronometro.focus()
    boton_iniciar["state"] ="disabled"
    boton_resetear["state"] = "disabled"
    boton_parar["state"] = "normal"




def parar_cronometro():


    global tarea
    
    rotulo_cronometro.after_cancel(tarea)


    boton_iniciar["state"] ="normal"
    boton_resetear["state"] = "normal"
    boton_parar["state"] = "disabled"




def resetear_cronometro():


    global horas, minutos, segundos


    horas, minutos, segundos = 0, 0, 0
    tiempo.set(f"{horas:02d}:{minutos:02d}:{segundos:02d}")


    boton_iniciar["state"] ="normal"
    boton_resetear["state"] = "disabled"
    boton_parar["state"] = "disabled"






##### CREACIÓN DEL CUADERNO #####


cuaderno = ttk.Notebook(ventana)
cuaderno.pack(expand = True, fill =tk.BOTH)




##### PAGINA 1 DEL CUADERNO #####


pagina_1 = tk.Frame(cuaderno, padx=2, pady=2)
cuaderno.add(pagina_1, text="  Fecha/Hora   ")




fecha = tk.StringVar()
rotulo_fecha = tk.Label(pagina_1,
    textvariable=fecha,
    font="arial 18 bold", 
    bg="black", fg="green")
rotulo_fecha.pack(expand=True, fill=tk.BOTH, ipadx=10, ipady=10)




hora = tk.StringVar()
rotulo_hora = tk.Label(pagina_1,
    textvariable=hora,
    font="arial 36",
    bg="black", fg="blue",
    anchor=tk.N)
rotulo_hora.pack(expand=True, fill=tk.BOTH, ipadx=5, ipady=5)




actualizar_hora()
actualizar_fecha()




##### PAGINA 2 DEL CUADERNO #####


pagina_2 = tk.Frame(cuaderno)
cuaderno.add(pagina_2, text="  Cronómetro  ")




tiempo = tk.StringVar()
tiempo.set(f"{horas:02d}:{minutos:02d}:{segundos:02d}")


rotulo_cronometro = tk.Label(pagina_2,
    textvariable=tiempo,
    font="arial 30", 
    bg="black", fg="blue")
rotulo_cronometro.pack(expand=True, fill=tk.BOTH)




frame_botones = tk.Frame(pagina_2)


boton_iniciar = tk.Button(frame_botones, 
    font="arial 10",
    text="Iniciar",
    width=7,
    bg="lightgrey", fg="red",
    command=iniciar_cronometro)
boton_iniciar.pack(padx=10, pady=10, side=tk.LEFT)


boton_parar = tk.Button(frame_botones, 
    font="arial 10",
    text="Parar",
    width=7,
    state="disabled",
    bg="lightgrey", fg="red",
    command=parar_cronometro)
boton_parar.pack(padx=10, pady=10, side=tk.LEFT)


boton_resetear = tk.Button(frame_botones, 
    font="arial 10",
    text = "Reset", 
    width=7,
    state="disabled",
    bg="lightgrey", fg="red",
    command=resetear_cronometro)
boton_resetear.pack(padx=10, pady=10, side=tk.LEFT)


frame_botones.pack()


##### BUCLE PRINCIPAL #####


ventana.mainloop()


