from bancomat import *
from utenti import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class BancomatApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Bancomat Molpol")
        self.root.geometry("500x650")
        window.resizable(False,False)
        root.configure(background="white")
    
    #GESTIONE FRAME
    self.frame1 = tk.Frame(master = window)
    self.frame1.pack()

    #TITOLO
    self.titolo = tk.Label(self.frame2, text ="Bancomat MolPol", background="light blue", width = 600, foreground="white", font=('Helvetica', 20), anchor= "center")
    self.titolo.pack()

window = tk.Tk()
BancomatApp(window)
window.mainloop()