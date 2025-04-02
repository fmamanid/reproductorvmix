import tkinter as tk
from tkinter import ttk
main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview(columns=("size", "lastmod"))
treeview.pack()
main_window.mainloop()