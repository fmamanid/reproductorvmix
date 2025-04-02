import tkinter as tk
from tkinter import messagebox, ttk
def show_info():
    # Obtener el texto del Elemento 1.
    text = treeview.item(my_iid, option="text")
    # Mostrarlo en un cuadro de diálogo.
    messagebox.showinfo(title="Información", message=text)
main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview()
my_iid = "id_unico"
treeview.insert("", tk.END, text="Elemento 1", iid=my_iid)
treeview.pack()
button = ttk.Button(text="Mostrar información", command=show_info)
button.pack()
main_window.mainloop()