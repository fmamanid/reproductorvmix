        
import tkinter as tk
from tkinter import ttk
import time
main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")
cont = 0
valor_variable =0
def actualiza(val):
    global valor_variable
    if val >=6:
        quit()
    grid.selection_set(grid.get_children()[val])
    print(f"funcion {val}")
    cont =val +1
    time.sleep(1)
    valor_variable = grid.after(3000, actualiza,cont)

def salir():
    print("se termino de ejecutar el bucle")
    grid.after_cancel(valor_variable)

grid =ttk.Treeview(main_window,columns=("col1","col2","col3"))
grid['selectmode']='browse'
grid.column("#0",width=50)
grid.column("col1",width=350)
grid.column("col2",width=400)
grid.column("col3",width=80)
#.grid.column("col4",width=90,anchor=CENTER)

grid.heading("#0",text="Item")
grid.heading("col1",text="Titulo")
grid.heading("col2",text="Ubicacion")
grid.heading("col3",text="Estado")
#self.grid.heading("col4",text="Country Code",anchor=CENTER)

grid.insert("",tk.END,text="1",values=('A Pesar De Mí  Alex Zurdo x Redimi2 x Funky Ft Un Corazón Indiomar Abby Valdez_1080p.mp4','D:/D/VideosCristianos/A Pesar De Mí  Alex Zurdo x Redimi2 x Funky Ft Un Corazón Indiomar Abby Valdez_1080p.mp4','Terminado'))
grid.insert("",tk.END,text="2",values=('Alex Zurdo  Fue Por Mi  En Vivo_1080p.mp4','D:/D/VideosCristianos/Alex Zurdo  Fue Por Mi  En Vivo_1080p.mp4','Reproduciendo'))
grid.insert("",tk.END,text="3",values=('Alex Zurdo  Te Siento Video Oficial_1080p.mp4','D:/D/VideosCristianos/Alex Zurdo  Te Siento Video Oficial_1080p.mp4','Pendiente'))
grid.insert("",tk.END,text="4",values=('A Pesar De Mí  Alex Zurdo x Redimi2 x Funky Ft Un Corazón Indiomar Abby Valdez_1080p.mp4','D:/D/VideosCristianos/A Pesar De Mí  Alex Zurdo x Redimi2 x Funky Ft Un Corazón Indiomar Abby Valdez_1080p.mp4','Terminado'))
grid.insert("",tk.END,text="5",values=('Alex Zurdo  Fue Por Mi  En Vivo_1080p.mp4','D:/D/VideosCristianos/Alex Zurdo  Fue Por Mi  En Vivo_1080p.mp4','Reproduciendo'))
grid.insert("",tk.END,text="6",values=('Alex Zurdo  Te Siento Video Oficial_1080p.mp4','D:/D/VideosCristianos/Alex Zurdo  Te Siento Video Oficial_1080p.mp4','Pendiente'))


boton = tk.Button(main_window, text="Salir", command=salir)
boton.pack()
grid.pack()


actualiza(0)

main_window.mainloop()