import tkinter as tk
from tkinter import ttk
main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview()
uno=treeview.insert("", tk.END, text="Elemento 1")
subuno= treeview.insert(uno, tk.END, text="Subelemento 1")
subuno1=treeview.insert(subuno, tk.END, text="Otro elemento")

dos=treeview.insert("", tk.END, text="Elemento 2")
tres=treeview.insert("", tk.END, text="Elemento 3")
cuatro=treeview.insert("", tk.END, text="Elemento 4")
print(uno)
print(subuno)
print(subuno1)
print(dos)
print(tres)
print(cuatro)
text = treeview.item(subuno1, option="text")
print(text)

treeview.focus(cuatro)  # Pone el foco en item.
print(treeview.focus())

treeview.pack()
main_window.mainloop()