from bancomat import *
from utenti import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class BancomatApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Bancomat Molpol")
        self.root.geometry("400x220")
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
         #TITOLO:
        self.btnLoad = tk.Button(self.frame1, text="Carica Dataset")
        self.btnLoad.grid(row=0,column=0)
    
        #CONFIGURAZIONE SECONDO FRAME
        #variabili di controllo username e password
        """self.user = tk.StringVar()
        self.psw = tk.StringVar()"""

        #Label e entry per username e password
        self.lblUser = tk.Label(self.frame2, text = 'Username', font=('calibre',10, 'bold'))
        self.ntrUser = tk.Entry(self.frame2, font=('calibre',10,'normal'))

        self.lblPsw = tk.Label(self.frame2, text = 'Password', font = ('calibre',10,'bold'))
        self.ntrPsw = tk.Entry(self.frame2, font = ('calibre',10,'normal'), show = '*')
        
        self.btnLogin = tk.Button(self.frame2, text="Login")

        #Inserimento nel grid layout
        self.lblUser.grid(row=0,column=0)
        self.ntrUser.grid(row=0,column=1)
        self.lblPsw.grid(row=1,column=0)
        self.ntrPsw.grid(row=1,column=1)
        self.btnLogin.grid(row=2,column=1)
        

        #CONFIGURAZIONE TERZO FRAME
        self.btnSaldo = tk.Button(self.frame3, text="Vedi saldo", state="disabled")
        self.btnPrelievo = tk.Button(self.frame3, text="Prelievo", state="disabled")
        self.btnDeposito = tk.Button(self.frame3, text="Deposita", state="disabled")
        self.btnTransf = tk.Button(self.frame3, text="Trasferisci cash", state="disabled")

        #Inserimento nel grid
        self.btnSaldo.grid(row=0, column=0, padx=15, pady=15)
        self.btnPrelievo.grid(row=0, column=1, padx=15, pady=15)
        self.btnDeposito.grid(row=0, column=2, padx=15, pady=15)
        self.btnTransf.grid(row=0, column=3, padx=15, pady=15)

        #BINDING
        self.btnLoad.bind("<Button-1>", self.caricaDataset)
        self.btnLogin.bind("<Button-1>", self.login)

        #VARIABILI DI CONTROLLO
        self.load = False
        self.check_login = False

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
                            messagebox.showinfo("Operazione riuscita", "File caricato con successo!")
                            self.load = True
            except IOError:
                messagebox.showerror("Attenzione", "Errore nel caricamento del file " + filename)
                return False 
            #return filename
        else:
            messagebox.showwarning("Attenzione", "Caricare il file in formato .txt")
            return False
        
    def login(self, event):
        if self.load:
            user = self.ntrUser.get().strip()
            psw = self.ntrPsw.get().strip()
            if user != "" and psw != "":
                if self.bancomat.login(user, psw):
                    messagebox.showinfo("Operazione riuscita", "Login effettuato con successo!")
                    self.check_login = True
                    #Attivo i button sotto
                    self.btnSaldo.config(state="normal")
                    self.btnDeposito.config(state="normal")
                    self.btnPrelievo.config(state="normal")
                    self.btnTransf.config(state="normal")
                else:
                    messagebox.showerror("Errore", "Login non effettuato. Per favore controlla le credenziali e riprova.")
            else:
                messagebox.showwarning("Attenzione", "Riempire i campi prima di premere sul Login")
        else:
            messagebox.showerror("Attenzione", "Per favore, carica il file prima di effettuare il login :)")
    
    #def vedi_saldo(self, event):


    def prelievo(self, event):
        if self.check_login:
            user = self.ntrUser.get().strip()
            psw = self.ntrPsw.get().strip()
            if self.bancomat.preleva(user, psw):
                messagebox.showinfo("Operazione riuscita", "Denaro prelevato con successo!")
            else:
                messagebox.showwarning("Attenzione", "Operazione di prelievo non riuscita!")
        else:
            messagebox.showerror("Attenzione", "Effettuare il login")
    
    def trasferisci(self, event):
        if self.check_login:
            user = self.ntrUser.get().strip()
            psw = self.ntrPsw.get().strip()
            if self.bancomat.preleva(user, psw):
                messagebox.showinfo("Operazione riuscita", "Denaro prelevato con successo!")
            else:
                messagebox.showwarning("Attenzione", "Operazione di prelievo non riuscita!")
        else:
            messagebox.showerror("Attenzione", "Effettuare il login")
   
    def deposita(self, event):    
        if self.check_login:
            user = self.ntrUser.get().strip()
            psw = self.ntrPsw.get().strip()
            if self.bancomat.deposita(user, psw):
                messagebox.showinfo("Operazione riuscita", "Denaro depositato con successo!")
            else:
                messagebox.showwarning("Attenzione", "Operazione di prelievo non riuscita!")
        else:
            messagebox.showerror("Attenzione", "Effettuare il login")

window = tk.Tk()
BancomatApp(window)
window.mainloop()