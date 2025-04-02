import tkinter as tk
from tkinter import ttk
import time




##### VENTANA PRINCIPAL #####


ventana = tk.Tk()
ventana.title("Reloj digital")
ventana.geometry("260x160+500+100")




##### FUNCIONES MENUS #####


aumentos = 0


def modo_aumentar():


    global aumentos


    aumentos += 1


    configurar_tamanio()




def modo_disminuir():


    global aumentos


    aumentos -= 1


    configurar_tamanio()




def configurar_tamanio():


    global aumentos


    if aumentos == 0:
        ventana.geometry("260x160+500+100")
        t_fecha, t_hora, t_crono, t_boton = 22, 36, 28, 10
        menu_tamanio.entryconfig(1, state="disabled")
    elif aumentos == 1:
        ventana.geometry("460x280+500+100")
        t_fecha, t_hora, t_crono, t_boton = 40, 68, 48, 18
        menu_tamanio.entryconfig(1, state="normal")
    elif aumentos == 2:
        ventana.geometry("580x340+500+100")
        t_fecha, t_hora, t_crono, t_boton = 52, 88, 58, 24
        menu_tamanio.entryconfig(0, state="normal")
    else:
        ventana.geometry("720x460+500+100")
        t_fecha, t_hora, t_crono, t_boton = 62, 108, 72, 36
        menu_tamanio.entryconfig(0, state="disabled")




    rotulo_fecha.config(font=("arial", t_fecha))
    rotulo_hora.config(font=("arial", t_hora))
    rotulo_cronometro.config(font=("arial", t_crono))
    boton_iniciar.config(font=("arial", t_boton))
    boton_parar.config(font=("arial", t_boton))
    boton_resetear.config(font=("arial", t_boton))






def modo_tema():
    if opcion_tema.get() == 1:
        rotulo_fecha.config(background="black")
        rotulo_hora.config(background="black")
        rotulo_cronometro.config(background="black")
    elif opcion_tema.get() == 2:
        rotulo_fecha.config(background="white")
        rotulo_hora.config(background="white")
        rotulo_cronometro.config(background="white")




def mostrar_fecha():


    if opcion_fecha.get():
        if opcion_hora.get():
            rotulo_hora.pack_forget()
            rotulo_fecha.pack(expand=True, fill=tk.BOTH, ipadx=5, ipady=5)
            rotulo_hora.pack(expand=True, fill=tk.BOTH, ipadx=10, ipady=10)
        else:
            rotulo_fecha.pack(expand=True, fill=tk.BOTH, ipadx=5, ipady=5)
    else:
        rotulo_fecha.pack_forget()




def mostrar_hora():


    if opcion_hora.get():
        rotulo_hora.pack(expand=True, fill=tk.BOTH, ipadx=5, ipady=5)
    else:
        rotulo_hora.pack_forget()




##### FUNCIONES RELOJ #####




def actualizar_hora():
    hora.set(time.strftime("%H:%M:%S"))
    rotulo_hora.after(200, actualizar_hora)
    rotulo_hora.focus()




def actualizar_fecha():
    fecha.set(time.strftime("%d / %m / %Y"))
    rotulo_fecha.after(200, actualizar_fecha)






##### FUNCIONES CRONOMETRO MEJORADO #####


inicio = 0
duracion = 0
tarea = None




def activar_cronometro():


    global inicio
    global duracion


    if duracion == 0:
        inicio = time.time()
    else:
        inicio = time.time() - duracion


    rotulo_cronometro.after(300, actualizar_cronometro)


    rotulo_cronometro.focus()
    boton_iniciar["state"] ="disabled"
    boton_resetear["state"] = "disabled"
    boton_parar["state"] = "normal"




def actualizar_cronometro():


    global inicio
    global tarea
    global duracion


    duracion = time.time() - inicio


    horas = int(duracion // 60 // 60)
    minutos = int(duracion // 60 % 60)
    segundos = int(duracion % 60)


    tiempo.set(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
    tarea = rotulo_cronometro.after(300, actualizar_cronometro)




def parar_cronometro():


    global tarea
    
    rotulo_cronometro.after_cancel(tarea)


    boton_iniciar["state"] ="normal"
    boton_resetear["state"] = "normal"
    boton_parar["state"] = "disabled"




def resetear_cronometro():


    global inicio
    global duracion


    inicio = 0
    duracion = 0


    tiempo.set(f"00:00:00")


    boton_iniciar["state"] ="normal"
    boton_resetear["state"] = "disabled"
    boton_parar["state"] = "disabled"






##### CREACIÓN DE LOS MENUS #####


opcion_tema = tk.IntVar()
opcion_tema.set(1)


opcion_fecha = tk.BooleanVar()
opcion_fecha.set(True)


opcion_hora = tk.BooleanVar()
opcion_hora.set(True)


barra_menus = tk.Menu(ventana)


menu_tamanio = tk.Menu(barra_menus, tearoff=0)
menu_tamanio.add_command(label="Aumentar", command=modo_aumentar)
menu_tamanio.add_command(label="Disminuir", state="disabled", command=modo_disminuir)
barra_menus.add_cascade(label="Tamaño", menu=menu_tamanio)


menu_tema = tk.Menu(barra_menus, tearoff=0)
menu_tema.add_radiobutton(label="Oscuro", value=1, variable=opcion_tema, command=modo_tema)
menu_tema.add_radiobutton(label="Claro", value=2, variable=opcion_tema, command=modo_tema)
barra_menus.add_cascade(label="Tema", menu=menu_tema)


menu_opciones = tk.Menu(barra_menus, tearoff=0)
menu_opciones.add_checkbutton(label="Fecha", variable=opcion_fecha, command=mostrar_fecha)
menu_opciones.add_checkbutton(label="Hora", variable=opcion_hora, command=mostrar_hora)
barra_menus.add_cascade(label="Opciones", menu=menu_opciones)


ventana.config(menu=barra_menus)






##### CREACIÓN DEL CUADERNO #####


cuaderno = ttk.Notebook(ventana)
cuaderno.pack(expand = True, fill =tk.BOTH)


##### Página 1 del Cuaderno #####


pagina_1 = tk.Frame(cuaderno, padx=2, pady=2)
cuaderno.add(pagina_1, text="  Fecha/Hora   ")




fecha = tk.StringVar()
rotulo_fecha = tk.Label(pagina_1,
    textvariable=fecha,
    font="arial 22", 
    bg="black", fg="green")
rotulo_fecha.pack(expand=True, fill=tk.BOTH, ipadx=5, ipady=5)




hora = tk.StringVar()
rotulo_hora = tk.Label(pagina_1,
    textvariable=hora,
    font="arial 36",
    bg="black", fg="blue")
rotulo_hora.pack(expand=True, fill=tk.BOTH, ipadx=10, ipady=10)








actualizar_hora()
actualizar_fecha()






##### Página 2 del Cuaderno #####


pagina_2 = tk.Frame(cuaderno, padx=2, pady=2)
cuaderno.add(pagina_2, text="  Cronómetro  ")


tiempo = tk.StringVar()
tiempo.set(f"00:00:00")


rotulo_cronometro = tk.Label(pagina_2,
    textvariable=tiempo,
    font="arial 28", 
    bg="black", fg="blue")
rotulo_cronometro.pack(expand=True, fill=tk.BOTH)


frame_botones = tk.Frame(pagina_2)


boton_iniciar = tk.Button(frame_botones, 
    font="arial 10",
    text="Iniciar",
    width=6,
    bg="lightgrey", fg="red",
    command=activar_cronometro)
boton_iniciar.pack(padx=10, pady=10, side=tk.LEFT)


boton_parar = tk.Button(frame_botones, 
    font="arial 10",
    text="Parar",
    width=6,
    state="disabled",
    bg="lightgrey", fg="red",
    command=parar_cronometro)
boton_parar.pack(padx=10, pady=10, side=tk.LEFT)


boton_resetear = tk.Button(frame_botones, 
    font="arial 10",
    text = "Reset", 
    width=6,
    state="disabled",
    bg="lightgrey", fg="red",
    command=resetear_cronometro)
boton_resetear.pack(padx=10, pady=10, side=tk.LEFT)


frame_botones.pack()




rotulo_cronometro.focus()




##### BUCLE PRINCIPAL #####


ventana.mainloop()
