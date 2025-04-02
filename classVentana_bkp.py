#instalar  pip install mutagen
#
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from classVideoVmix import *
from classLogoVmix import *
import funcion
import mutagen




class Ventana (Frame):


    def __init__(self, master = None):
        super().__init__(master, width=1000, height=260)
        self.master=master
        self.pack()
        self.create_widgets()

###############3  VARIABLES ############

    tiempo_inicio = 0
    duracion_video = 0
    tarea_rotulo_tiempo = None
##############################################################################
########################  FUNCIONES BOTON PLAY ###############################
##############################################################################

    def actualiza_rotulo_tiempo(self):
        diferencia =int(round(time.time() - self.tiempo_inicio)) 
        self.rotulo_tiempo.configure(text=diferencia)
        self.tarea_rotulo_tiempo = self.rotulo_tiempo.after(300, self.actualiza_rotulo_tiempo)
        if self.nro_reg > self.ultimo_registro:
            self.rotulo_tiempo.after_cancel(self.tarea_rotulo_tiempo)



    def funcion_boton_play(self):
        self.nro_reg=0
        self.cant_total = len(self.mi_lista.get_children())
        self.ultimo_registro = len(self.mi_lista.get_children())
        self.nro_reg = 0
        self.mi_lista.after(300, self.test)
        self.rotulo_tiempo.after(300, self.actualiza_rotulo_tiempo)
        self.btn_load.configure(state="disabled")
        self.btn_clear.configure(state="disabled")
        self.btn_play.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        

    terminar_ciclo = True
    
    tiempo_del_video =5

    tareaTest =0

    termino_el_video = True

    actualizo_el_rotulo_de_la_lista = True

    def test(self):

        if self.actualizo_el_rotulo_de_la_lista:
            #print(f" Funcion actualizo_el_rotulo_de_la_lista nro_reg: {self.nro_reg}")
            if self.nro_reg >= self.ultimo_registro:
                self.actualiza_rotulos_mi_lista(self.ultimo_registro-1)
            else:
                self.actualiza_rotulos_mi_lista(self.nro_reg)

            self.actualizo_el_rotulo_de_la_lista = False
            self.tareaTest = self.mi_lista.after(300, self.test)

        
        if self.termino_el_video:
            #print(f"tiempo_del_video: {self.tiempo_del_video} \n")
            print(f"######### EMITIR VIDEO: numero de registro: {self.nro_reg} ##################")
            self.reproduce_un_registro_de_mi_lista(self.nro_reg)
            self.nro_reg +=1
            self.termino_el_video = False
            if self.nro_reg >= self.ultimo_registro:
                self.mi_lista.after_cancel(self.tareaTest)
                self.parar_lista()

            else:
                self.tareaTest = self.mi_lista.after(300, self.test)
        else:
            tiempo_transcurrido = time.time() - self.tiempo_inicio
            if tiempo_transcurrido > self.duracion_video:
                print("ESPERAMOS A QUE TERMINE EL VIDEO")
                self.termino_el_video = True
                self.actualizo_el_rotulo_de_la_lista = True
                #self.tiempo_del_video = 5
                self.tareaTest = self.mi_lista.after(300, self.test)
            else:
                print(f"timepo {self.tiempo_del_video}")
                self.tiempo_del_video -= 1
                self.tareaTest = self.mi_lista.after(300, self.test)
                
                


    def actualiza_rotulos_mi_lista(self, nro_reg):
        id_fila = self.mi_lista.get_children()[nro_reg]
        self.mi_lista.selection_set(id_fila)
        info = self.mi_lista.item(id_fila)
        valores = info['values']
        self.rotulo_nombre['text']=valores[0]
        self.rotulo_duracion['text']=valores[1]
        self.rotulo_ubicacion['text']=valores[2]

    ###########  ESTE ES UN BUCLE DE MI LISTA ##################
    def actualiza_mi_lista(self, nro_bucle):

        nro_reg = self.cant_total - nro_bucle
        print(f"item lista {nro_reg}")
        utlimo_reg = self.cant_total - 1
        self.actualiza_rotulos_mi_lista(nro_reg)

        self.reproduce_un_registro_de_mi_lista(nro_reg)

        nro_bucle=nro_bucle-1
        if nro_bucle == 0:
            self.mi_lista.after_cancel(self.tarea_mi_lista)
        else:
            self.tarea_mi_lista = self.mi_lista.after(1000, self.actualiza_mi_lista, nro_bucle)





    def reproduce_un_registro_de_mi_lista(self, nro_registro):
        utlimo_reg = len(self.mi_lista.get_children()) - 1
        print(f"###############   {nro_registro}   ################")
        if nro_registro == 0:
            #self.actualiza_rotulos_nombre(self.nro_reg)
            v_preview = self.get_ubicacion_reg(nro_registro+1)
            v_out = self.get_ubicacion_reg(nro_registro)
            v_del = ""
            print(v_preview)
            print(v_out)
            print(v_del)
            self.emitir_video(v_preview, v_out, v_del, 1)
            #time.sleep(1)
            #self.tiempo_bucle += 1
            #self.nro_reg += 1
            #self.after_cancel(self.tarea)
            #self.vista_reg = self.nro_reg
        elif nro_registro== utlimo_reg:
            #self.actualiza_rotulos_nombre(self.nro_reg)
            v_preview = ""
            v_out = self.get_ubicacion_reg(nro_registro)
            v_del = self.get_ubicacion_reg(nro_registro-1)
            self.emitir_video(v_preview, v_out, v_del, 3)
            print(v_preview)
            print(v_out)
            print(v_del)    
            #time.sleep(1)
            #self.nro_reg += 1      
            #self.vista_reg = utlimo_reg              
        elif nro_registro == utlimo_reg+1:
            #self.actualiza_rotulos_nombre(self.nro_reg-2)
            v_preview = ""
            v_out = ""
            v_del = self.get_ubicacion_reg(nro_registro-1)
            self.emitir_video(v_preview, v_out, v_del, 4)
            print(v_preview)
            print(v_out)
            print(v_del)       
            #time.sleep(1)
            #self.nro_reg += 1   
            #self.vista_reg = utlimo_reg              
        elif nro_registro > utlimo_reg+1:
            #self.vista_reg = utlimo_reg 
            print(f"####SALIENDO   {self.nro_reg}   SALIENDO####3")
            #self.after_cancel(self.mi_tarea)
            
            #time.sleep(1)
            #self.nro_reg += 1            
        else:
            #self.actualiza_rotulos_nombre(self.nro_reg)
            v_preview = self.get_ubicacion_reg(nro_registro+1)
            v_out = self.get_ubicacion_reg(nro_registro)
            v_del = self.get_ubicacion_reg(nro_registro-1)
            self.emitir_video(v_preview, v_out, v_del, 2)
            print(v_preview)
            print(v_out)
            print(v_del)
            #time.sleep(1)
            #self.vista_reg = self.nro_reg

    def emitir_video(self, v_Preview, v_Out, v_Del, opcion):
        ####  INCIALIZAMOS LOS OBJETOS VMIX ###########
        videoPreviewVmix = AppVideoVmix(v_Preview)
        videoOutVmix = AppVideoVmix(v_Out )
        videoDelVmix = AppVideoVmix(v_Del )
        miLogo = AppLogoVmix(variables.direccionLogo)
        if opcion == 1:
            videoOutVmix.cargarVideo()
            time.sleep(1)
            videoPreviewVmix.cargarVideo()
            time.sleep(1)
            videoOutVmix.reproducirVideo()
            
            self.duracion_video = funcion.duracion_video(v_Out)

            self.tiempo_inicio = time.time()

            miLogo.reproduceLogo(videoOutVmix.nombreArchivo)
            time.sleep(1)
            videoPreviewVmix.cargarPreview()
            
            
            
            self.fin_del_video=False
            self.tiempo_bucle = 0

        elif opcion == 2:
            videoDelVmix.esperarVideo()
            videoOutVmix.reproducirVideo()
            
            self.duracion_video = funcion.duracion_video(v_Out)

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
            self.fin_del_video=False
            self.tiempo_bucle = 0

        elif opcion == 3:
            videoDelVmix.esperarVideo()
            videoOutVmix.reproducirVideo()
            
            self.duracion_video = funcion.duracion_video(v_Out)

            self.tiempo_inicio = time.time()
            
            miLogo.reproduceLogo(videoOutVmix.nombreArchivo)
            time.sleep(1)
            videoDelVmix.cerrarVideo()
            self.tiempo_del_video = funcion.duracion_video(v_Out)+5
            self.fin_del_video=False
            self.tiempo_bucle = 0            

        elif opcion == 4:
            videoDelVmix.esperarVideo()
            time.sleep(1)
            videoDelVmix.cerrarVideo()
            
            self.fin_del_video=False
            self.tiempo_bucle = 0  



##############################################################################
########################  FUNCIONES BOTON LOAD ###############################
#############################################################################


    def mi_lista_get_dir():
        pass


    def get_nombre_reg(self,nro_reg):
        id_fila = self.mi_lista.get_children()[nro_reg]
        #self.mi_lista.selection_set(id_fila)
        info = self.mi_lista.item(id_fila)
        valores = info['values']
        nombre = valores[0]
        return nombre

    def get_duracion_reg(self,nro_reg):
        id_fila = self.mi_lista.get_children()[nro_reg]
        #self.mi_lista.selection_set(id_fila)
        info = self.mi_lista.item(id_fila)
        valores = info['values']
        duracion = valores[1]
        return duracion
    
    def get_ubicacion_reg(self,nro_reg):
        id_fila = self.mi_lista.get_children()[nro_reg]
        #self.mi_lista.selection_set(id_fila)
        info = self.mi_lista.item(id_fila)
        valores = info['values']
        ubicacion = valores[2]
        return ubicacion



    def actualiza_tiempo(self):
        self.rotulo_tiempo['text']=str(self.tiempo_bucle)

    mi_tarea = 0





##################  FUNCION ACTUALIZA LA VENTANA #############################

    def actualizaMiVentana(self, n_ciclos):
        # En esta seccion debemos de colocar los witches que deseamos actualizar
        self.rotulo_tiempo['text']=str(n_ciclos)

        # Eso lo dejamos para el buble de control
        n_ciclos=n_ciclos-1
        if n_ciclos == 0:
            self.after_cancel(self.mi_tarea)
        else:
            self.mi_tarea = self.after(1000, self.actualizaMiVentana,n_ciclos)
               

    def actualiza_miLista(self,item):
        id_fila = self.mi_lista.get_children()[item]
        self.mi_lista.selection_set(id_fila)

    def esperar_video(self, nombre_videoa_esperar):
        videoEsperarVmix = AppVideoVmix(nombre_videoa_esperar)
        if len(nombre_videoa_esperar) != 0:
            print(f"ESPERAR HASTA QUE SE REPRODUSCA EL VIDEO\n{nombre_videoa_esperar}")
            videoEsperarVmix.esperarVideo()
            #esperarVideo(videoOut) 


####################### BUBLE PRINCIPAL PARA EMITER EL VIDEO ########

    tiempo_bucle = 0


    se_actualizo_la_lista = False

    nro_reg = 0
    vista_reg = 0









    # def actualiza_ventana(self):
    #     self.actualiza_tiempo()
               
    #     utlimo_reg = self.cant_total - 1

    #     if not(self.se_actualizo_la_lista):

    #         if self.nro_reg > utlimo_reg:
    #             self.actualiza_rotulos_nombre(utlimo_reg) 
    #             self.actualiza_miLista(utlimo_reg)
    #             #print(f"ultiomo regitro {self.nro_reg}")
    #         else:
    #             self.actualiza_rotulos_nombre(self.vista_reg) 
    #             self.actualiza_miLista(self.vista_reg)         
    #         self.se_actualizo_la_lista = True
    #         self.tarea = self.after(200, self.actualiza_ventana)
       

    #     ####################3  EJECUTA EN VMIX ##############333333333
    #     if self.tiempo_bucle > self.tiempo_video + 10:
    #         #self.actualiza_miLista(self.vista_reg)
    #         #self.fin_del_video = True

    #         self.se_actualizo_la_lista = False

    #         print(f"###############   {self.nro_reg}   ################")
    #         if self.nro_reg == 0:
    #             #self.actualiza_rotulos_nombre(self.nro_reg)
    #             v_preview = self.get_ubicacion_reg(self.nro_reg+1)
    #             v_out = self.get_ubicacion_reg(self.nro_reg)
    #             v_del = ""
    #             print(v_preview)
    #             print(v_out)
    #             print(v_del)
    #             self.emitir_video(v_preview, v_out, v_del, 1)
    #             time.sleep(1)
    #             self.tiempo_bucle += 1
    #             #self.nro_reg += 1
    #             #self.after_cancel(self.tarea)
    #             #self.vista_reg = self.nro_reg
    #         elif self.nro_reg == utlimo_reg:
    #             #self.actualiza_rotulos_nombre(self.nro_reg)
    #             v_preview = ""
    #             v_out = self.get_ubicacion_reg(self.nro_reg)
    #             v_del = self.get_ubicacion_reg(self.nro_reg-1)
    #             self.emitir_video(v_preview, v_out, v_del, 3)
    #             print(v_preview)
    #             print(v_out)
    #             print(v_del)    
    #             time.sleep(1)
    #             #self.nro_reg += 1      
    #             #self.vista_reg = utlimo_reg              
    #         elif self.nro_reg == utlimo_reg+1:
    #             #self.actualiza_rotulos_nombre(self.nro_reg-2)
    #             v_preview = ""
    #             v_out = ""
    #             v_del = self.get_ubicacion_reg(self.nro_reg-1)
    #             self.emitir_video(v_preview, v_out, v_del, 4)
    #             print(v_preview)
    #             print(v_out)
    #             print(v_del)       
    #             time.sleep(1)
    #             #self.nro_reg += 1   
    #             #self.vista_reg = utlimo_reg              
    #         elif self.nro_reg > utlimo_reg:
    #             #self.vista_reg = utlimo_reg 
    #             print(f"####SALIENDO   {self.nro_reg}   SALIENDO####3")
    #             self.after_cancel(self.tarea)
                
    #             time.sleep(1)
    #             #self.nro_reg += 1            
    #         else:
    #             #self.actualiza_rotulos_nombre(self.nro_reg)
    #             v_preview = self.get_ubicacion_reg(self.nro_reg+1)
    #             v_out = self.get_ubicacion_reg(self.nro_reg)
    #             v_del = self.get_ubicacion_reg(self.nro_reg-1)
    #             self.emitir_video(v_preview, v_out, v_del, 2)
    #             print(v_preview)
    #             print(v_out)
    #             print(v_del)
    #             time.sleep(1)
    #             #self.vista_reg = self.nro_reg
    #         self.vista_reg = self.nro_reg
    #         self.nro_reg += 1
    #         #self.vista_reg += 1

        
    #     self.tiempo_bucle += 1
    #     #print(self.tiempo_bucle )
    #     #funciones.imprimir()

    #     ##############  bulbe infinito ################

    #     if self.nro_reg > utlimo_reg +2:
    #         #self.mi_lista.after_cancel(self.tarea)
    #         self.after_cancel(self.tarea)
    #     else:
    #         #self.tarea = self.mi_lista.after(2000, self.actualiza_lista, nro_reg)
    #         self.tarea = self.after(1000, self.actualiza_ventana)





##################  FUNCIONES DE LOS BOTONES ##################################        

    def abrir_carpeta(self):
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
                print(f"es un archivo es {funcion.nombre_video(linea)}")
                f = open(linea, "r")
                dir_videos = f

            elif linea.find(".mp4") > 0:
                print(f"el archivo es {funcion.nombre_video(linea)}")
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
        for linea in dir_videos:
            i+=1
            aux = linea.replace("\n","")
            print(aux)
            direccion = aux
            nombre = funcion.nombre_video(aux)
            self.cargar_datos(i,nombre,direccion)
        #print(direcion)


    def limpiar_lista(self):
        self.btn_load.configure(state="normal")
        self.btn_clear.configure(state="disabled")
        self.btn_play.configure(state="disabled")
        self.mi_lista.delete(*self.mi_lista.get_children())
        self.after(1000, self.fuuncion_test)


    def fuuncion_test(self):
        pass

    def parar_lista(self):
        
        self.mi_lista.after_cancel(self.tareaTest)
        self.rotulo_tiempo.after_cancel(self.tarea_rotulo_tiempo)
        self.btn_play.configure(state="normal")
        self.btn_clear.configure(state="normal")
        self.btn_stop.configure(state="disabled")
        

    def retroceder (self):
        pass
    def siguiente(self):
        #self.mi_tarea = self.after(1000, self.actualizaMiVentana,100)
        pass

    def salir(self):
        quit()

    def cargar_datos(self, nro_reg, dato_reg, dir_dato):
        log = funcion.duracion_video(dir_dato)
        #print(f"el video tiene {minutos} [min] con {segundos} [s]")
        minutos, segundos = divmod(log, 60)
        dur_formateado = f"{int(round(minutos,0))}:{int(round(segundos,0))}"
        self.mi_lista.insert('',END, text=f'{nro_reg}',values=(f'{dato_reg}',f'{dur_formateado}',f'{dir_dato}','Pendiente'))
        self.btn_load.configure(state="disabled")
        self.btn_clear.configure(state="normal")
        self.btn_play.configure(state="normal")







##########################  FUNCIONES DEL LOGO ##############################3

    def abrir_dir_logo(self):
        direccion = filedialog.askopenfilename(initialdir='/',
                                          title='Abrir logo',
                                          filetypes=(('Archivo de logo','*.xaml'),('Archivo de Imagen','*.png'))
                                          )
        
        #self.rotulo_dir_logo=Label(ventana_logo,text="Direccion del logo ..",

        self.rotulo_dir_logo.configure(text=direccion)
        if len(direccion)==0:
            messagebox.showwarning("Abrir","Debe seleccionar un archivo")
        else:
            variables.direccionLogo = direccion
            miLogo = AppLogoVmix(variables.direccionLogo)
            miLogo.cargarLogo()
            #messagebox.showwarning("Abrir",f"Debe seleccionar un archivo\n{variables.direccionLogo} ")

    def guardaCriterio(self):
        nuevoCriterio = self.txtCriterio.get()        
        variables.criterioLogo = nuevoCriterio
        messagebox.showinfo("Criterio",f"Se guardo el nuevo criterioi\n{nuevoCriterio}")
        self.txtCriterio.configure(state="disabled")
        self.btnEditarCriterio.configure(state="normal")
        self.btnGuargarCriterio.configure(state="disabled")

    def editarCriterio(self):

        self.txtCriterio.configure(state="normal")
        self.btnEditarCriterio.configure(state="disabled")
        self.btnGuargarCriterio.configure(state="normal")






##########################  WIDGETS PRINCIPAL ###################################
    def create_widgets(self):
        ##### CREACIÓN DEL CUADERNO #####


        cuaderno = ttk.Notebook(self)
        cuaderno.pack(expand = True, fill =BOTH)

        ##### PAGINA 1 DEL CUADERNO #####


        pagina_1 = Frame(cuaderno, padx=2, pady=2)
        cuaderno.add(pagina_1, text="   Reproductor   ")



        ############## PRIMER CUADRO ###################
        frame1=Frame(self)
        #frame1.pack(expand=True,fill="both")
        ############# ROTULO TITULO ####################
        
        rotulo_titulo = Label(pagina_1,
                              text='AUTOMATIZADOR VMIX',
                              relief="groove",
                              font="consolas 20 bold",
                              padx=20, pady=10,
                              bd=2)
        rotulo_titulo.pack()
        frame1.pack(padx=20,pady=20)

        ############## PRIMER CUADRO ###################
        frame2=Frame(pagina_1)
        frame2.pack(expand=True,fill="both")

        ############# ROTULO LISTA DE REPRODUCCION#######        
        rotulo_lista = Label(frame2,
                             text='LISTA DE REPRODUCCION',
                             font="consolas 14 bold")
        rotulo_lista.pack(side="left")

        frame2.pack()

        ############## SEGUNDO CUADRO ###################
        frame3=Frame(pagina_1)
 	

        ############# TABLA LISTA DE REPRODUCCION####### 

        self.mi_lista = ttk.Treeview(frame3, 
                                  columns=('col1','col2','col3','col4'))
        self.mi_lista.column('#0',width=50)
        self.mi_lista.column('col1',width=400)
        self.mi_lista.column('col2',width=50)
        self.mi_lista.column('col3',width=200)
        self.mi_lista.column('col4',width=50)

        self.mi_lista.heading('#0',text='ITEM')
        self.mi_lista.heading('col1',text='NOMBRE')
        self.mi_lista.heading('col2',text='DURACION')
        self.mi_lista.heading('col3',text='UBICACION')
        self.mi_lista.heading('col4',text='ESTADO')

        self.mi_lista.pack(side="left",padx=2, pady=2, fill=BOTH)

        sb=Scrollbar(frame3,orient='vertical')
        sb.pack(side='right',fill=Y)
        self.mi_lista.configure(yscrollcommand=sb.set)
        sb.config(command=self.mi_lista.yview)
        self.mi_lista['selectmode']='browse'
        frame3.pack(fill=BOTH)





        ############## TERCER  CUADRO ###################
        frame4=Frame(pagina_1,
                     bg="lightblue",
                     padx=10, pady=10
                     )

        self.rotulo_nombre_titulo = Label(frame4,
                              text='NOMBRE DEL VIDEO: ',
                              bg="lightblue",
                              #anchor=W,
                              width=20,
                              #textvariable=self.nomdre_del_video
                              )
        self.rotulo_nombre_titulo.grid(column=0,row=0)

        self.rotulo_nombre = Label(frame4,
                              text='',
                              bg="lightblue",
                              #anchor=W,
                              width=100,
                              #textvariable=self.nomdre_del_video
                              )
        self.rotulo_nombre.grid(column=1,row=0)

        self.rotulo_ubicacion_titulo = Label(frame4,
                                 text='UBICACION DEL VIDEO',
                                 width=20,
                                 anchor="w",
                                 bg="lightblue")
        self.rotulo_ubicacion_titulo.grid(row=1,column=0, padx=10, pady=10)

        self.rotulo_ubicacion = Label(frame4,
                                 text='',
                                 width=100,
                                 anchor="w",
                                 bg="lightblue")
        self.rotulo_ubicacion.grid(row=1, column=1, padx=10, pady=10)        

        #rotulo_barra = Label(frame4,
        #                      text='**************',
        #                      bg="red",
        #                      width=50)
        #rotulo_barra.grid(row=0,column=1)
        self.barra_tiempo = ttk.Progressbar(frame4, 
                                 orient= 'horizontal', 
                                 length = 350, 
                                 mode='determinate',
                                 maximum=50,
                                 style="Horizontal.TProgressbar")
        #self.barra_tiempo .step(99)
        self.barra_tiempo .grid(row=2,column=1)

        self.rotulo_tiempo = Label(frame4,
                                 text='00:00/',
                                 width=5,
                                 anchor=W,
                                 bg="lightblue")
        self.rotulo_tiempo.grid(padx=10, pady=10, row=2,column=2)

        self.rotulo_duracion = Label(frame4,
                                text='00:00',
                                bg="lightblue",
                                anchor=E,
                                width=5)
        self.rotulo_duracion.grid(row=2, column=3)


        


        frame4.pack(expand=True,fill='both')



        ############## CUARTO CUADRO ###################
        frame5=Frame(pagina_1)

        self.btn_load = Button(frame5,text='LOAD',
                          width=10, height=5,
                          command=self.abrir_carpeta)
        self.btn_load.grid(row=0, column=0,padx=5,pady=5)

        self.btn_clear = Button(frame5,text='CLEAR',
                          width=10, height=5,
                          command=self.limpiar_lista,
                          state="disabled")
        self.btn_clear.grid(row=0, column=1,padx=5,pady=5)

        self.btn_play = Button(frame5,text='PLAY', 
                          width=10, height=5,
                          #bg="green",
                          #fg="white",
                          state="disabled",
                          command=self.funcion_boton_play)
        self.btn_play.grid(row=0, column=2,padx=5,pady=5)


        self.btn_stop = Button(frame5,text='STOP', 
                          width=10,height=5,
                          #bg="red",
                          #fg="black",
                          #font="consolas 14 bold",
                          state="disabled",
                          command=self.parar_lista)
        self.btn_stop.grid(row=0, column=3,padx=5,pady=5)


        self.btn_back = Button(frame5,text='BACK', 
                          width=10,height=5,
                          command=self.retroceder,
                          state="disabled")
        self.btn_back.grid(row=0, column=4,padx=5,pady=5)


        self.btn_next = Button(frame5,text='NEXT', 
                          width=10,height=5,
                          command=self.siguiente,
                          state="disabled")
        self.btn_next.grid(row=0, column=5,padx=5,pady=5)


        btn_exit = Button(frame5,text='EXIT', 
                          width=10,height=5,
                          command=self.salir)
        btn_exit.grid(row=0, column=6,padx=5,pady=5)

        frame5.pack()
 



        ##### PAGINA 2 DEL CUADERNO #####


        pagina_2 = Frame(cuaderno)
        cuaderno.add(pagina_2, text="     Logo     ")

        ventana_logo = Frame(pagina_2)

        rotulo_titulo = Label(ventana_logo,
                              text='CARGA LOGO DE VMIX',
                              relief="groove",
                              font="consolas 20 bold",
                              padx=20, pady=10,
                              bd=2)
        rotulo_titulo.pack(padx=20,pady=10)


        self.rotulo_dir_logo=Label(ventana_logo,text="Direccion del logo ..",
                              font="consolas 14",
                              bg="lightblue")
  
        self.rotulo_dir_logo.pack(padx=20,pady=10)

        

        btn_abrir_dir_logo = Button(ventana_logo,text="ABRIR",
                                    width=10,
                                    height=5,
                                    command=self.abrir_dir_logo)
        btn_abrir_dir_logo.pack(padx=20,pady=10)

        self.lblCriterio=Label(ventana_logo,text="Criterio del logo",
                              font="consolas 14",
                              bg="lightblue")
  
        self.lblCriterio.pack(padx=20,pady=10)

        name_var = StringVar()
        name_var.set(variables.criterioLogo)
        self.txtCriterio = Entry(ventana_logo, 
                                 textvariable = name_var, 
                                 font=('calibre',10,'normal'),
                                 state="disabled")
        self.txtCriterio.pack()


        frame6 =Frame(ventana_logo)

        self.btnEditarCriterio = Button(ventana_logo, 
                                    text="Editar", 
                                    font="consolas 12 bold", 
                                    command=self.editarCriterio)
        self.btnEditarCriterio.pack()

        self.btnGuargarCriterio = Button(ventana_logo, 
                                    text="Guardar", 
                                    font="consolas 12 bold", 
                                    state="disabled",
                                    command=self.guardaCriterio)
        self.btnGuargarCriterio.pack()
        
        frame6.pack()
        ventana_logo.pack()

        ##### PAGINA 3 DEL CUADERNO #####


        pagina_3 = Frame(cuaderno)
        cuaderno.add(pagina_3, text="  Conexion  ")


