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
        #self.cliccato_var = tk.BooleanVar(value=False)

        #Utilizzo di grid per posizionare il frame principale
        """self.frame = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.pack()"""

        # Creazione dei frame che suddividono la window
        self.frame1 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame2 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame3 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)

        # Posizionamento dei frame all'interno della finestra principale
        self.frame1.grid(row=0, column=0, padx=10, pady=10)
        self.frame2.grid(row=1, column=0, padx=10, pady=10)
        self.frame3.grid(row=2, column=0, padx=10, pady=10)

        #Configuro il frame alla grandezza dell'intera finestra
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #Widget dentro il primo frame
        self.btnLoad = tk.Button(self.frame1, text="Carica Dataset")
        self.btnLoad.grid(row=0,column=0)
    
        #CONFIGURAZIONE SECONDO FRAME
        #variabili di controllo username e password
        self.user = tk.StringVar()
        self.psw = tk.StringVar()

        #Label e entry per username e password
        self.lblUser = tk.Label(self.frame2, text = 'Username', font=('calibre',10, 'bold'))
        self.ntrUser = tk.Entry(self.frame2,textvariable = self.user, font=('calibre',10,'normal'))

        self.lblPsw = tk.Label(self.frame2, text = 'Password', font = ('calibre',10,'bold'))
        self.ntrPsw = tk.Entry(self.frame2, textvariable = self.psw, font = ('calibre',10,'normal'), show = '*')
        
        self.btnLogin = tk.Button(self.frame2, text="Login")

        #Inserimento nel grid layout
        self.lblUser.grid(row=0,column=0)
        self.ntrUser.grid(row=0,column=1)
        self.lblPsw.grid(row=1,column=0)
        self.ntrPsw.grid(row=1,column=1)
        self.btnLogin.grid(row=2,column=1)
        

        #CONFIGURAZIONE TERZO FRAME
        self.btnSaldo = tk.Button(self.frame3, text="Vedi saldo")
        self.btnPrelievo = tk.Button(self.frame3, text="Prelievo")
        self.btnDeposito = tk.Button(self.frame3, text="Deposita")
        self.btnTransf = tk.Button(self.frame3, text="Trasferisci cash")

        #Inserimento nel grid
        self.btnSaldo.grid(row=0, column=0, padx=15, pady=15)
        self.btnPrelievo.grid(row=0, column=1, padx=15, pady=15)
        self.btnDeposito.grid(row=0, column=2, padx=15, pady=15)
        self.btnTransf.grid(row=0, column=3, padx=15, pady=15)

        #Creazione oggetto Bancomat
        #self.userAdmin = ""
        #self.pswAdmin = ""
        #self.btnLoad = Admin(userAdmin, pswAdmin)
        #userAdmin, pswAdmin, filename = self.caricaDataset()
        """systemAdmin = Admin(userAdmin, pswAdmin)"""
        #self.bancomat = Bancomat(systemAdmin, 0, 0)
        """bancomat.carica_da_file(userAdmin, pswAdmin, filename)"""
        #print(bancomat)

        #CAMPI DA COMPLETARE:
        
        #BOTTONI
        
        #bottone che mi permette di caricare il file.txt
        """self.btnLoad = tk.Button(self.frame, text="Carica Dataset")
        self.btnLoad.grid(row=2, column=2, padx=2, pady=2)"""

        #BINDING
        #self.btnLoad.bind("<Button-1>", self.caricaDataset)

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