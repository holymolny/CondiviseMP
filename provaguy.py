from bancomat import *
from utenti import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class BancomatApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Bancomat Molpol")
        self.cliccato_var = tk.BooleanVar(value=False)

        #Creazione oggetto Bancomat
        self.userAdmin = ""
        self.pswAdmin = ""
        #self.btnLoad = Admin(userAdmin, pswAdmin)
        #userAdmin, pswAdmin, filename = self.caricaDataset()
        """systemAdmin = Admin(userAdmin, pswAdmin)"""
        #self.bancomat = Bancomat(systemAdmin, 0, 0)
        """bancomat.carica_da_file(userAdmin, pswAdmin, filename)"""
        #print(bancomat)

        #Utilizzo di grid per posizionare il frame principale
        self.frame = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame.grid(row=0, column=0, sticky="nsew")


        #DEFINISCO LO STILE UNICO DEI BOTTONI
        """  style = ttk.Style() #classe fornita dal modulo tk per lo stile
        style.configure('StileBottoni', foreground='blue', font=('Helvetica', 12))"""

        #CAMPI DA COMPLETARE:
        
        #BOTTONI
        
        #bottone che mi permette di caricare il file.txt
        self.btnLoad = ttk.Button(self.frame, text="Carica Dataset")
        self.btnLoad.grid(row=2, column=2, padx=2, pady=2)

        #BINDING
        self.btnLoad.bind("<Button-1>", self.caricaDataset)

        




    #FUNZIONI
    
    #1 - Carica il dataset
    def caricaDataset(self, event=None):
        #Carica il file:
        filePath = filedialog.askopenfilename()
        filePath = filePath.strip() #elimina eventuali spazi bianchi a inizio e fine stringa
        indiceBarra = filePath.rfind("/") #restituisce l'ultimo indice di "/"
        filename = filePath[indiceBarra + 1:]
        #print(filename)
        indicePunto = filename.rfind(".") 
        estensione = filename[indicePunto + 1:]
        if estensione == "txt":
            try:
            #carico il file in lettura e prendo solo User e Psw dell'ADMIN e filename 
                with open(filename, "r") as file:
                    for riga in file:
                        riga = riga.strip()
                        if riga.startswith("Admin:"):
                            user, psw = riga.split()[1:3]
                            self.userAdmin = user
                            self.pswAdmin = psw
                            self.bancomat = Bancomat(Admin(self.userAdmin, self.pswAdmin), 0, 0)
                            print(self.bancomat) 
                            print(self.bancomat.carica_da_file(self.userAdmin, self.pswAdmin, filename))
                            #Cosi prende in considereazione solo il primo admin che trova
                            exit
                            #print(self.bancomat)S
            except IOError:
                messagebox.showwarning("Attenzione", "Errore nel caricamento del file " + filename)
                return False 
            #return filename
        else:
            messagebox.showwarning("Attenzione", "Caricare il file in formato .txt")
            return False

       

window = tk.Tk()
BancomatApp(window)
window.mainloop()