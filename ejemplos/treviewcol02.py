import tkinter as tk
from tkinter import ttk
main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview(columns=("size", "lastmod"))

treeview.heading("#0", text="Archivo")
treeview.heading("size", text="Tamaño")
treeview.heading("lastmod", text="Última modificación")

item1=treeview.insert(
    "",
    tk.END,
    text="README.txt",
    values=("1 bytes", "18:30")
)
item2=treeview.insert(
    "",
    tk.END,
    text="LEEME.txt",
    values=("2 bytes", "18:30")
)
item3=treeview.insert(
    "",
    tk.END,
    text="NOLOLEAS.txt",
    values=("3 bytes", "18:30")
)
print(treeview.set(item3,"size","100 bytes"))
treeview.pack()
main_window.mainloop()