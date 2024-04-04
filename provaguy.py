from bancomat import *
from utenti import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class BancomatApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Bancomat Molpol")
        self.root.geometry("800x600")
        self.cliccato_var = tk.BooleanVar(value=False)

        #Utilizzo di grid per posizionare il frame principale
        """self.frame = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.pack()"""

        #GRID:
        for i in range(3):
            window.columnconfigure(i, weight=1, minsize=75)
            window.columnconfigure(i, weight=1, minsize=50)
            if (i==3):
                for j in range(4):
                    frame = tk.Frame(
                        master = window,
                        relief = tk.RAISED,
                        borderwidth=1
                    )
        frame.grid(row=i, column=j, padx = 5, pady = 5) #padding
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
            

        #PROVA MOLNY
        name_var=tk.StringVar()
        passw_var=tk.StringVar()

        name_label = tk.Label(self.frame, text = 'Username', font=('calibre',10, 'bold'))
        name_entry = tk.Entry(self.frame,textvariable = name_var, font=('calibre',10,'normal'))
        passw_label = tk.Label(self.frame, text = 'Password', font = ('calibre',10,'bold'))
        passw_entry=tk.Entry(self.frame, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
        sub_btn=tk.Button(self.frame,text = 'Login')
    
        name_label.grid(row=0,column=0)
        name_entry.grid(row=0,column=1)
        passw_label.grid(row=1,column=0)
        passw_entry.grid(row=1,column=1)
        sub_btn.grid(row=2,column=1)

        #Creazione oggetto Bancomat
        self.userAdmin = ""
        self.pswAdmin = ""
        #self.btnLoad = Admin(userAdmin, pswAdmin)
        #userAdmin, pswAdmin, filename = self.caricaDataset()
        """systemAdmin = Admin(userAdmin, pswAdmin)"""
        #self.bancomat = Bancomat(systemAdmin, 0, 0)
        """bancomat.carica_da_file(userAdmin, pswAdmin, filename)"""
        #print(bancomat)

        #CAMPI DA COMPLETARE:
        
        #BOTTONI
        
        #bottone che mi permette di caricare il file.txt
        self.btnLoad = tk.Button(self.frame, text="Carica Dataset")
        self.btnLoad.grid(row=2, column=2, padx=2, pady=2)

        #BINDING
        self.btnLoad.bind("<Button-1>", self.caricaDataset)

    #FUNZIONI
    
    #1 - Carica il dataset
    def caricaDataset(self, event):
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
                            self.bancomat.carica_da_file(self.userAdmin, self.pswAdmin, filename)
                            #Cosi prende in considereazione solo il primo admin che trova
                            return True
            except IOError:
                messagebox.showerror(tk.messagebox.ERROR, "Attenzione", "Errore nel caricamento del file " + filename)
                return False 
            #return filename
        else:
            messagebox.showwarning("Attenzione", "Caricare il file in formato .txt")
            return False

    """ def login():
        username = self.name_var.get()
        password = self.password_var.get()
        print("The name is : " + name)
        print("The password is : " + password)
        name_var.set("")
        passw_var.set("")  """

window = tk.Tk()
BancomatApp(window)
window.mainloop()