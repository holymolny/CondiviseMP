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
        self.frame1 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1, background="light blue")
        self.frame2 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1, background="green")
        self.frame3 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1, background = "pink")
        self.frame4 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1, background= "yellow")
        

        # Posizionamento dei frame all'interno della finestra principale
        self.frame1.grid(row=0, column=0, padx=10, pady=10)
        self.frame2.grid(row=1, column=1, padx=10, pady=10)
        self.frame3.grid(row=1, column=2, padx=10, pady=10)
        self.frame4.grid(row=1, column=3, padx=10, pady=10)
        """self.frame5.grid(row=4, column=0, padx=10, pady=10)
        self.frame6.grid(row=5, column=0, padx=10, pady=10)
        self.frame6.grid(row=6, column=0, padx=10, pady=10)"""
        

        #Configuro il frame alla grandezza dell'intera finestra
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)



        #CONFIGURAZIONE PRIMO FRAME
        self.titolo = tk.Label(
            self.frame1,
            text ="Bancomat MolPol",
            padx=0,
            pady=0,
            width = 300,
            height= 100,
            background="light blue",
            foreground="white",
            font=('Helvetica', 50)
            )
        self.titolo.pack()
        self.btnLoad = tk.Button(self.frame1, text="Carica Dataset", background="light blue", width=20)
        self.btnLoad.pack()

        
        
        #CONFIGURAZIONE SECONDO FRAME
        
        #Label e entry per username e password
        
        self.lblUser = tk.Label(self.frame2, text = 'Username', font=('calibre',10, 'bold'), state="disabled")
        self.ntrUser = tk.Entry(self.frame2, font=('calibre',10,'normal'), state="disabled")

        self.lblPsw = tk.Label(self.frame2, text = 'Password', font = ('calibre',10,'bold'), state="disabled")
        self.ntrPsw = tk.Entry(self.frame2, font = ('calibre',10,'normal'), show = '*', state="disabled")
        
        #self.btnLogin = tk.Button(self.frame2, text="Login", state="disabled")

        #Inserimento nel grid layout
        self.lblUser.grid(row=0,column=0)
        self.ntrUser.grid(row=0,column=1)
        self.lblPsw.grid(row=1,column=0)
        self.ntrPsw.grid(row=1,column=1)
        #self.btnLogin.grid(row=2,column=1)    

        """self.lblUser.pack(side = tk.TOP)
        self.ntrUser.pack(side = tk.TOP)
        self.lblPsw.pack(side = tk.TOP)
        self.ntrPsw.pack(side = tk.TOP)"""
        #self.btnLogin.pack(side = tk.LEFT)


        #CONFIGURAZIONE TERZO FRAME
        self.btnLimite = tk.Button(self.frame3, text="Vedi limite", background="light blue", width=20, padx=10, pady=10, state="disabled")
        self.btnScoperto = tk.Button(self.frame3, text="Vedi scoperto", background="light green", width=20, padx=10, pady=10, state="disabled")
        self.btnPrelievo = tk.Button(self.frame3, text="Prelievo", background="light green", width=20, padx=10, pady=10, state="disabled")
        self.btnDeposito = tk.Button(self.frame3, text="Deposita", background="light green", width=20, padx=10, pady=10, state="disabled")
        self.btnTransf = tk.Button(self.frame3, text="Trasferisci cash", background="light green", width=20, padx=10, pady=10, state="disabled")

        #Inserimento nel grid

        self.btnLimite.pack(side = tk.TOP)
        self.btnScoperto.pack(side = tk.TOP)
        self.btnPrelievo.pack(side = tk.TOP)
        self.btnDeposito.pack(side = tk.TOP)
        self.btnTransf.pack(side = tk.TOP)
        """self.btnLimite.grid(row=1, column=0, padx=15, pady=15)
        self.btnScoperto.grid(row=2, column=0, padx=15, pady=15)
        self.btnPrelievo.grid(row=3, column=0, padx=15, pady=15)
        self.btnDeposito.grid(row=4, column=0, padx=15, pady=15)
        self.btnTransf.grid(row=5, column=0, padx=15, pady=15)"""

        #CONFIGURAZIONE QUARTO FRAME
        self.limitevar = tk.StringVar()
        self.lblLimite = tk.Label(self.frame4, text = 'Username', font=('calibre',10, 'bold'), textvariable=self.limitevar)
        
        self.lblLimite.pack_forget()


        
        


        """self.btnLimite.grid(row=0, column=0, padx=15, pady=15)
        self.btnScoperto.grid(row=0, column=1, padx=15, pady=15)
        self.btnPrelievo.grid(row=0, column=2, padx=15, pady=15)
        self.btnDeposito.grid(row=0, column=3, padx=15, pady=15)
        self.btnTransf.grid(row=0, column=4, padx=15, pady=15)"""

        #BINDING
        self.btnLoad.bind("<Button-1>", self.caricaDataset)
        self.btnLimite.bind("<Button-1>", self.mostraLimite)
        self.btnScoperto.bind("<Button-1>", self.mostraScoperto)
        self.btnPrelievo.bind("<Button-1>", self.prelievo)
        self.btnDeposito.bind("<Button-1>", self.deposita)
        self.btnTransf.bind("<Button-1>", self.trasferisci)
        #self.btnLogin.bind("<Button-1>", self.login)

        

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
                            if self.bancomat.carica_da_file(self.userAdmin, self.pswAdmin, filename):
                                #Messaggio di buon fine
                                messagebox.showinfo("Operazione riuscita", "File caricato con successo!")

                                #Abilita il login
                                self.lblUser.config(state="normal")
                                self.ntrUser.config(state="normal")
                                self.lblPsw.config(state="normal")
                                self.ntrPsw.config(state="normal")

                                #Abilita i button per le operazioni
                                self.btnLimite.config(state="normal")
                                self.btnScoperto.config(state="normal")
                                self.btnDeposito.config(state="normal")
                                self.btnPrelievo.config(state="normal")
                                self.btnTransf.config(state="normal")

                                #Cosi prende in considerazione solo il primo admin che trova
                                break
                            else:
                                messagebox.showerror("Attenzione", "Errore nel caricamento del file " + filename) 
                            """self.btnLimite.config(state="normal")
                            self.btnScoperto.config(state="normal")
                            self.btnDeposito.config(state="normal")
                            self.btnPrelievo.config(state="normal")
                            self.btnTransf.config(state="normal")"""
            except IOError:
                messagebox.showerror("Attenzione", "Errore nel caricamento del file " + filename)
                return False 
            #return filename
        else:
            messagebox.showwarning("Attenzione", "Caricare il file in formato .txt")
            return False
        

    def mostraLimite(self, event):
        #Attivazione dei campi per effettuare il login
        user = self.ntrUser.get().strip()
        psw = self.ntrPsw.get().strip()
        if self.bancomat.get_limite_prelievo(user, psw):
            self.lblLimite.pack(side = tk.TOP)
            self.limitevar.set("Limite prelievo = ")

        else:
            messagebox.showerror("Attenzione", "Credenziali errate, controlla se sono giuste e riprova")

    def mostraScoperto(self, event):
        user = self.ntrUser.get().strip()
        psw = self.ntrPsw.get().strip()
        if self.bancomat.get_scoperto_massimo(user, psw):
            messagebox.showinfo("Operazione riuscita", "Limite denaro è: " + str(self.bancomat.get_limite_prelievo(user, psw)))
        else:
            messagebox.showerror("Attenzione", "Credenziali errate, controlla se sono giuste e riprova")

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