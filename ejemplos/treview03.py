import tkinter as tk
from tkinter import ttk
def show_info():
    # Imprime los elementos del árbol.
    treeview_children = treeview.get_children()
    print(treeview_children)
    # Imprime los elementos dentro del Elemento 1.
    item_children = treeview.get_children(item)
    print(item_children)
main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview()
item = treeview.insert("", tk.END, text="Elemento 1")
treeview.insert(item, tk.END, text="Subelemento 1")
treeview.pack()
button = ttk.Button(text="Mostrar información", command=show_info)
button.pack()
main_window.mainloop()