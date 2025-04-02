import tkinter as tk
from tkinter import ttk, messagebox
import time
import funcionones_btn
import classVideoVmix
import classLogoVmix
import variables
import funcion
from datetime import datetime, timedelta
from time import gmtime, strftime
import classReproduccionVmix

#############  VARIABLES  #############

tiempo_acumulado_en_segundos = 0



###  FUNCIONES DE LOS BOTONES ######
miLista =[]
def Agregar():
    global miLista
    miLista = funcionones_btn.Agregar()
    print(f"mi lista toal {len(miLista)}")
    for i in miLista:
        print(i.direccion)

    cargar_datos(miLista)

    print("Algo paso")

lista_de_videos =[]

def cargar_datos(una_lista):
    i=0

    global tiempo_acumulado_en_segundos
    global lista_de_videos

    txt_hora_inicio = rotulo_empieza.get()
    #messagebox.showinfo("Actulaizar hora",f"la hora se actualizara a: {txt_hora_inicio}")

    formato_mihora = datetime.strptime(txt_hora_inicio,"%d/%m/%Y %H:%M:%S")

    tiempo_inicio_lista = formato_mihora # datetime.now()
    
    #strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

    tiempo_acumulado_en_segundos = 0

    lista_de_videos =[]
    for unVideo in una_lista:
        
        #tiempo_inicio_lista = time.strftime("%d/%m/%Y %H:%M:%S")

        tiempo_adicional = timedelta(seconds=tiempo_acumulado_en_segundos)

        tiempo_inicio_video =  tiempo_inicio_lista + tiempo_adicional
        
        fecha_hora_cadena = tiempo_inicio_video.strftime("%d/%m/%Y %H:%M:%S")  
        #strftime("%d/%m/%Y %H:%M:%S",tiempo_inicio_lista)  # date.fromtimestamp(tiempo_inicio_lista)
        
        #(time.strftime("%d / %m / %Y") + " 00:00:00" )
        dur_formateado = f"{unVideo.duracionMinutos}:{unVideo.duracionSegundos}"
        #print(dur_formateado)
        mi_lista.insert('',tk.END, text=f'{unVideo.nombre}',values=(f'{fecha_hora_cadena}',f'{dur_formateado}','Video',f'{unVideo.direccion}'))
        text_lista = (f'{unVideo.nombre}',f'{fecha_hora_cadena}',f'{dur_formateado}',"Video",f'{unVideo.direccion}')
        lista_de_videos.append(text_lista)
        tiempo_acumulado_en_segundos = tiempo_acumulado_en_segundos + unVideo.duracionVideo
    
    tiempo_adicional = timedelta(seconds=tiempo_acumulado_en_segundos)
    tiempo_inicio_video =  tiempo_inicio_lista + tiempo_adicional
    fecha_hora_cadena = tiempo_inicio_video.strftime("%d/%m/%Y %H:%M:%S")  

    tiempo_final.set(fecha_hora_cadena)

    btn_load.configure(state="disabled")
    btn_clear.configure(state="normal")
    btn_play.configure(state="normal")
    
    


def Limpiar():
    btn_load.configure(state="normal")
    btn_clear.configure(state="disabled")
    btn_play.configure(state="disabled")
    mi_lista.delete(*mi_lista.get_children())
    ventana.after(1000, fuuncion_test)

def fuuncion_test():
    print("actulaziando ventana")


nro_reg = 0
cant_total = 0
ultimo_registro = 0
actualizo_el_rotulo_de_la_lista = True
termino_el_video = True
tiempo_inicio = 0
tiempo_duracion_video =0
tarea_bucle_principal = None

tarea_rotulo_tiempo =None

def Reproducir():
    global nro_reg
    global cant_total
    global ultimo_registro
    global actualizo_el_rotulo_de_la_lista
    global tarea_bucle_principal

    actualizo_el_rotulo_de_la_lista = True
    cant_total = len(mi_lista.get_children())
    ultimo_registro = len(mi_lista.get_children())
    nro_reg = 0

    mi_lista.after(300, actualiza_rotulos_mi_lista)

    tarea_bucle_principal = mi_lista.after(300, bucle_principal)

    #rotulo_tiempo.after(300, self.actualiza_rotulo_tiempo)
    btn_load.configure(state="disabled")
    btn_clear.configure(state="disabled")
    btn_play.configure(state="disabled")
    btn_stop.configure(state="normal")



def bucle_principal():
    global actualizo_el_rotulo_de_la_lista
    global nro_reg
    global ultimo_registro
    global termino_el_video
    global tiempo_inicio
    global tiempo_duracion_video
    global tarea_bucle_principal
    
    if termino_el_video:
        #print(f"tiempo_del_video: {self.tiempo_del_video} \n")
        print(f"######### EMITIR VIDEO: numero de registro: {nro_reg} ##################")
        reproduce_un_registro_de_mi_lista(nro_reg)

        termino_el_video = False
        if nro_reg >= ultimo_registro:
            mi_lista.after_cancel(tarea_bucle_principal)
            Detener()

        else:
            tarea_bucle_principal = mi_lista.after(300, bucle_principal)
    else:
        tiempo_transcurrido = time.time() - tiempo_inicio
        if tiempo_transcurrido > tiempo_duracion_video:
            print("ESPERAMOS A QUE TERMINE EL VIDEO")
            nro_reg +=1
            termino_el_video = True
            actualizo_el_rotulo_de_la_lista = True
            tarea_bucle_principal = mi_lista.after(300, bucle_principal)
        else:
            tarea_bucle_principal = mi_lista.after(300, bucle_principal)
                    

def actualiza_rotulos_mi_lista():
    global ultimo_registro
    global nro_reg
    miRegistro = 0
    if nro_reg >= ultimo_registro:
        miRegistro = ultimo_registro-1
    else:
        miRegistro = nro_reg
    id_fila = mi_lista.get_children()[miRegistro]
    mi_lista.selection_set(id_fila)
    info = mi_lista.item(id_fila)
    nombre = info["text"]
    titulo_video.set(nombre)
    valores = info['values']
    inicio_video.set(valores[0])
    duracion_video.set(valores[1])
    mi_lista.after(300, actualiza_rotulos_mi_lista)


def reproduce_un_registro_de_mi_lista(nro_registro):
    global tiempo_inicio
    global tiempo_duracion_video
    reproduccion = classReproduccionVmix.AppReproduccionVmix(lista_de_videos,nro_registro)
    reproduccion.reproducir_video()
    tiempo_duracion_video = reproduccion.tiempo_duracion_video
    tiempo_inicio = reproduccion.tiempo_inicio


def Detener(): ###################################################
    global tarea_bucle_principal
    mi_lista.after_cancel(tarea_bucle_principal)
    #rotulo_tiempo.after_cancel(tarea_rotulo_tiempo)
    btn_play.configure(state="normal")
    btn_clear.configure(state="normal")
    btn_stop.configure(state="disabled")

cont = 0
def Salir():
    quit()


##### FUNCIONES RELOJ #####




def actualizar_hora():
    hora.set(time.strftime("%H:%M:%S"))
    rotulo_hora.after(200, actualizar_hora)
    #rotulo_hora.focus()




def actualizar_fecha_hora():
    fecha_hora.set(time.strftime("%d / %m / %Y") + " 00:00:00" )
    rotulo_empieza.after(200, actualizar_fecha_hora)



def actualiza_fecha_fin():
    rotulo_termina.after(200, actualiza_fecha_fin)



def actualizar_hora_inicio():
    txt_hora_inicio = rotulo_empieza.get()
    messagebox.showinfo("Actulaizar hora",f"la hora se actualizara a: {txt_hora_inicio}")

    formato_mihora = datetime.strptime(txt_hora_inicio,"%d/%m/%Y %H:%M:%S")

    if datetime.now() >  formato_mihora:
        print("No se puede por que la hora configurad es menor a la fecha actrual")
    else:
        print(formato_mihora)



##### VENTANA PRINCIPAL #####


ventana = tk.Tk()
ventana.title("Automatizacion Vmix")
ventana.geometry("1000x600")
#ventana.minsize(width=600, height=600)
ventana.resizable(0,0)


##### CREACIÓN DE LOS MENUS #####


barra_menus = tk.Menu(ventana)


menu_archivo = tk.Menu(barra_menus, tearoff=0)
menu_archivo.add_command(label="Salir")
#menu_archivo.add_command(label="Disminuir", state="disabled")
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)


menu_edicion = tk.Menu(barra_menus, tearoff=0)
menu_edicion.add_command(label="Añadir")
menu_edicion.add_command(label="Mezclar")
barra_menus.add_cascade(label="Edicion", menu=menu_edicion)


menu_opciones = tk.Menu(barra_menus, tearoff=0)
menu_opciones.add_command(label="Enviar Vmix")
menu_opciones.add_command(label="Ajustes")
barra_menus.add_cascade(label="Opciones", menu=menu_opciones)

menu_ayuda = tk.Menu(barra_menus, tearoff=0)
menu_ayuda.add_command(label="Manual")
menu_ayuda.add_command(label="Sobre...")
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(menu=barra_menus)



##### CREACIÓN DEL CUADERNO #####


cuaderno = ttk.Notebook(ventana)
cuaderno.pack(expand = True, fill =tk.BOTH)


##### Página 1 del Cuaderno #####


pagina_1 = tk.Frame(cuaderno, padx=2, pady=2)
cuaderno.add(pagina_1, text="Principal")

frame_izquierda = tk.Frame(pagina_1)

frameLista=tk.Frame(frame_izquierda)
mi_lista = ttk.Treeview(frameLista, 
                            columns=('col1','col2','col3','col4'),
                            height=22)
mi_lista.column('#0',width=350)
mi_lista.column('col1',width=50)
mi_lista.column('col2',width=50)
mi_lista.column('col3',width=50)
mi_lista.column('col4',width=150)

mi_lista.heading('#0',text='Titulo')
mi_lista.heading('col1',text='Inicio')
mi_lista.heading('col2',text='Duracion')
mi_lista.heading('col3',text='Tipo')
mi_lista.heading('col4',text='Ubicacion')

mi_lista.pack(side="left",padx=2, pady=2, fill="y")

sb=tk.Scrollbar(frameLista,orient='vertical')
sb.pack(side='right',fill="y")
mi_lista.configure(yscrollcommand=sb.set)
sb.config(command=mi_lista.yview)
mi_lista['selectmode']='browse'

frameLista.pack(side="top", fill="x")


######  LOS BOTONES  ################
frame_botones =tk.Frame(frame_izquierda)


btn_load = tk.Button(frame_botones,text='Agregar',
                    width=10, height=5,
                    command=Agregar
                    )
btn_load.grid(row=0, column=0,padx=5,pady=5)

btn_clear = tk.Button(frame_botones,text='Limpiar',
                    width=10, height=5,
                    state="disabled",
                    command=Limpiar
                    )
btn_clear.grid(row=0, column=1,padx=5,pady=5)

btn_play = tk.Button(frame_botones,text='Reproducir', 
                    width=10, height=5,
                    #bg="green",
                    #fg="white",
                    state="disabled",
                    command=Reproducir)
btn_play.grid(row=0, column=2,padx=5,pady=5)


btn_stop = tk.Button(frame_botones,text='Detener', 
                    width=10,height=5,
                    #bg="red",
                    #fg="black",
                    #font="consolas 14 bold",
                    state="disabled",
                    command=Detener
                    )
btn_stop.grid(row=0, column=3,padx=5,pady=5)


btn_back = tk.Button(frame_botones,text='Atras', 
                    width=10,height=5,
                    state="disabled")
btn_back.grid(row=0, column=4,padx=5,pady=5)


btn_next = tk.Button(frame_botones,text='Adelante', 
                    width=10,height=5,
                    state="disabled")
btn_next.grid(row=0, column=5,padx=5,pady=5)


btn_exit = tk.Button(frame_botones,text='Salir', 
                    width=10,height=5,
                    command=Salir)
btn_exit.grid(row=0, column=6,padx=5,pady=5)



frame_botones.pack(side="bottom")

frame_izquierda.pack(side="left", fill="both")



frame_derecha = tk.Frame(pagina_1 )

frame_fecha_hora = tk.Frame(frame_derecha)


cuadro_fecha_hora = tk.LabelFrame(frame_derecha,
                                   #bg="green",
                                   width=350, height=300,
                                   text="Configuracion del tiempo",
                                   font="Arial 10 underline"
                                   )
hora = tk.StringVar()
rotulo_hora = tk.Label(cuadro_fecha_hora,
                              textvariable=hora,
                              bg="white",
                              font="consolas 14 bold",
                              width=8,
                              #textvariable=self.nomdre_del_video
                              )
rotulo_hora.grid(row=0,column=0, padx=5,pady=5, sticky="w")
btn_hora_actual = tk.Button(cuadro_fecha_hora,
                            text="Actualizar",
                            command=actualizar_hora_inicio)
btn_hora_actual.grid(row=0, column=1, padx=5,pady=5, sticky="e")


rotulo_empieza_titulo = tk.Label(cuadro_fecha_hora,
                              text='Empieza: ',
                              font="consolas 12 bold",
                              #bg="lightblue",
                              #anchor=W,
                              width=8,
                              padx=2, pady=2
                              #textvariable=self.nomdre_del_video
                              )
rotulo_empieza_titulo.grid(row=1,column=0)
fecha_hora = tk.StringVar()
fecha_hora.set(time.strftime("%d/%m/%Y %H:%M:%S"))
rotulo_empieza = tk.Entry(cuadro_fecha_hora,
                              textvariable=fecha_hora,
                              font="consolas 10",
                              bg="white",
                              #anchor=W,
                              width=20
                              #textvariable=self.nomdre_del_video
                              )
rotulo_empieza.grid(row=1,column=1, pady=5)



rotulo_termina_titulo = tk.Label(cuadro_fecha_hora,
                              text='Termina: ',
                              #bg="lightblue",
                              #anchor=W,
                              width=8,
                              padx=2, pady=2
                              #textvariable=self.nomdre_del_video
                              )
rotulo_termina_titulo.grid(row=2,column=0, sticky="e")
tiempo_final = tk.StringVar()
tiempo_final.set(time.strftime("%d/%m/%Y %H:%M:%S"))
rotulo_termina = tk.Label(cuadro_fecha_hora,
                              textvariable=tiempo_final,
                              bg="white",
                              #anchor=W,
                              width=20
                              #textvariable=self.nomdre_del_video
                              )
rotulo_termina.grid(row=2,column=1, padx=5,pady=5,sticky="e")


cuadro_fecha_hora.pack(fill="both")

frame_fecha_hora.pack()





frame_opciones_vmix = tk.Frame(frame_derecha)

btn_enviar_a_vmix = tk.Button(frame_opciones_vmix,
                              text="Enviar a Vmix",
                              width=15
                              )
btn_enviar_a_vmix.grid(row=0, column=0, padx=2,pady=2)

btn_borrar_lista_vmix = tk.Button(frame_opciones_vmix,
                              text="Borrar",
                              width=15
                              )
btn_borrar_lista_vmix.grid(row=0, column=1, padx=2,pady=2)

frame_opciones_vmix.pack()





cuadro_propiedades = tk.LabelFrame(frame_derecha,
                                   #bg="lightblue",
                                   width=300, height=300,
                                   text="Propiedades del video",
                                   font="Arial 10 underline"
                                   )


rotulo_nombre_titulo = tk.Label(cuadro_propiedades,
                              text='Titulo: ',
                              #bg="lightblue",
                              #anchor=W,
                              width=8,
                              padx=2, pady=2
                              #textvariable=self.nomdre_del_video
                              )
rotulo_nombre_titulo.grid(row=0,column=0)

titulo_video=tk.StringVar()





rotulo_nombre = tk.Label(cuadro_propiedades,
                              textvariable=titulo_video,
                              bg="white",
                              font="consolas 10",
                              #anchor=W,
                              width=33
                              #textvariable=self.nomdre_del_video
                              )
rotulo_nombre.grid(row=0,column=1, padx=5,pady=5)



rotulo_hora_inicio_titulo = tk.Label(cuadro_propiedades,
                              text='Hora inicio: ',
                              #bg="lightblue",
                              #anchor=W,
                              width=8
                              #textvariable=self.nomdre_del_video
                              )
rotulo_hora_inicio_titulo.grid(row=1, column=0)
inicio_video=tk.StringVar()
rotulo_hora_inicio = tk.Label(cuadro_propiedades,
                              textvariable=inicio_video,
                              bg="white",
                              width=20
                              #textvariable=self.nomdre_del_video
                              )
rotulo_hora_inicio.grid(row=1,column=1, padx=5,pady=5, sticky="w")



rotulo_duracion_titulo = tk.Label(cuadro_propiedades,
                              text='Duracion: ',
                              #bg="lightblue",
                              #anchor=W,
                              width=8,
                              #textvariable=self.nomdre_del_video
                              )
rotulo_duracion_titulo.grid(row=2, column=0)
duracion_video =tk.StringVar()
rotulo_duracion = tk.Label(cuadro_propiedades,
                              textvariable=duracion_video,
                              bg="white",
                              #anchor=W,
                              width=20,
                              #textvariable=self.nomdre_del_video
                              )
rotulo_duracion.grid(row=2,column=1, padx=5,pady=5, sticky="w")



rotulo_hora_final_titulo = tk.Label(cuadro_propiedades,
                              text='Hora final: ',
                              #bg="lightblue",
                              #anchor=W,
                              width=8,
                              #textvariable=self.nomdre_del_video
                              )
rotulo_hora_final_titulo.grid(row=3, column=0)
final_video =tk.StringVar()
rotulo_hora_final = tk.Label(cuadro_propiedades,
                              textvariable=final_video,
                              bg="white",
                              #anchor=W,
                              width=20,
                              #textvariable=self.nomdre_del_video
                              )
rotulo_hora_final.grid(row=3,column=1, padx=5,pady=5, sticky="w")



cuadro_propiedades.pack(fill="both",pady=5)



frame_propiedades_entrada = tk.Frame(frame_derecha)


cuadro_detalles_video = tk.LabelFrame(frame_derecha,
                                   #bg="green",
                                   width=300, height=300,
                                   text="Detalles",
                                   font="Arial 10 underline"
                                   )
detalles_video=tk.StringVar()
rotulo_detalles_video = tk.Label(cuadro_detalles_video,
                              textvariable=detalles_video,
                              bg="white",
                              #anchor=W,
                              width=100, height=20
                              #textvariable=self.nomdre_del_video
                              )

rotulo_detalles_video.pack(fill="both")

cuadro_detalles_video.pack()


frame_derecha.pack(side="right", fill="both")




 	
























##### Página 2 del Cuaderno #####


pagina_2 = tk.Frame(cuaderno, padx=2, pady=2)
cuaderno.add(pagina_2, text="Logo")



##### BUCLE PRINCIPAL #####

actualizar_hora()
#actualizar_fecha_hora()

ventana.mainloop()
