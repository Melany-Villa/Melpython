import tkinter as tk 
from tkinter import messagebox
from tkimter import ttk 

def mostrarmensaje():
    messagebox.showinfo("Haz click aqui", "melany")
    root = tk.TK()
    root.title("Haz click aqui")
    root.geometry("300x200")
    

button = tk.Button ( root,text="precionar aqui",comand=mostrarmensaje)
button.pack (pady=20)
   
progressbar = ttk.progressbar(root,orient="horizontal",length=200,mode="determinado")
root.mainloop()
