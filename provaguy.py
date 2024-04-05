from bancomat import *
from utenti import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class BancomatApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Bancomat Molpol")
        self.root.geometry("600x420")
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
        #TITOLO
        self.btnLoad = tk.Button(self.frame1, text="Carica Dataset")
        self.btnLoad.grid(row=0,column=0)


        #CONFIGURAZIONE SECONDO FRAME

        self.btnLimite = tk.Button(self.frame3, text="Vedi limite", state="disabled")
        self.btnScoperto = tk.Button(self.frame3, text="Vedi scoperto", state="disabled")
        self.btnPrelievo = tk.Button(self.frame3, text="Prelievo", state="disabled")
        self.btnDeposito = tk.Button(self.frame3, text="Deposita", state="disabled")
        self.btnTransf = tk.Button(self.frame3, text="Trasferisci cash", state="disabled")

        #Inserimento nel grid
        self.btnLimite.grid(row=0, column=0, padx=15, pady=15)
        self.btnScoperto.grid(row=0, column=1, padx=15, pady=15)
        self.btnPrelievo.grid(row=0, column=2, padx=15, pady=15)
        self.btnDeposito.grid(row=0, column=3, padx=15, pady=15)
        self.btnTransf.grid(row=0, column=4, padx=15, pady=15)
        

        #CONFIGURAZIONE TERZO FRAME
        
        #Label e entry per username e password
        self.lblUser = tk.Label(self.frame2, text = 'Username', font=('calibre',10, 'bold'), state="disabled")
        self.ntrUser = tk.Entry(self.frame2, font=('calibre',10,'normal'), state="disabled")

        self.lblPsw = tk.Label(self.frame2, text = 'Password', font = ('calibre',10,'bold'), state="disabled")
        self.ntrPsw = tk.Entry(self.frame2, font = ('calibre',10,'normal'), show = '*', state="disabled")
        
        self.btnLogin = tk.Button(self.frame2, text="Login", state="disabled")

        #Inserimento nel grid layout
        self.lblUser.grid(row=0,column=0, )
        self.ntrUser.grid(row=0,column=1)
        self.lblPsw.grid(row=1,column=0)
        self.ntrPsw.grid(row=1,column=1)
        self.btnLogin.grid(row=2,column=1)    



        #BINDING
        self.btnLoad.bind("<Button-1>", self.caricaDataset)
        self.btnLimite.bind("<Button-1>", self.mostraLimite)
        self.btnScoperto.bind("<Button-1>", self.mostraScoperto)
        self.btnPrelievo.bind("<Button-1>", self.prelievo)
        self.btnDeposito.bind("<Button-1>", self.deposita)
        self.btnTransf.bind("<Button-1>", self.trasferisci)
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
                            self.btnLimite.config(state="normal")
                            self.btnScoperto.config(state="normal")
                            self.btnDeposito.config(state="normal")
                            self.btnPrelievo.config(state="normal")
                            self.btnTransf.config(state="normal")
            except IOError:
                messagebox.showerror("Attenzione", "Errore nel caricamento del file " + filename)
                return False 
            #return filename
        else:
            messagebox.showwarning("Attenzione", "Caricare il file in formato .txt")
            return False
        
    def attivazioneLogin(self, event):
        #Attivazione dei campi per effettuare il login
        self.lblUser.config(state="normal")
        self.lblPsw.config(state="normal")
        self.ntrUser.config(state="normal")
        self.ntrPsw.config(state="normal")
        self.btnLogin.config(state="normal")    


    def login(self, event):
        if self.load:
            user = self.ntrUser.get().strip()
            psw = self.ntrPsw.get().strip()
            if user != "" and psw != "":
                if self.bancomat.login(user, psw):
                    messagebox.showinfo("Operazione riuscita", "Login effettuato con successo!")
                    self.check_login = True
                    #Attivo i button sotto
                    
                else:
                    messagebox.showerror("Errore", "Login non effettuato. Per favore controlla le credenziali e riprova.")
            else:
                messagebox.showwarning("Attenzione", "Riempire i campi prima di premere sul Login")
        else:
            messagebox.showerror("Attenzione", "Per favore, carica il file prima di effettuare il login :)")
    
    def mostraLimite(self, event):
        #Attivazione dei campi per effettuare il login
        self.attivazioneLogin(event)

        user = self.ntrUser.get().strip()
        psw = self.ntrPsw.get().strip()
        #if self.bancomat.get_limite_prelievo(user, psw):

    def mostraScoperto(self, event):
        self.attivazioneLogin(event)


    def prelievo(self, event):
        self.attivazioneLogin(event)
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
        self.attivazioneLogin(event)
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
        self.attivazioneLogin(event)   
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