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
    
    #GESTIONE FRAME
        self.frame1 = tk.Frame(master = window)
        self.frame1.pack()
        #FRAME CARICA-DATASET
        self.frame2 = tk.Frame(master=window)
        self.frame2.pack()
        #FRAME SPAZIO
        self.frame3 = tk.Frame(master=window)
        self.frame3.pack()
        #FRAME LOGIN
        self.frame4 = tk.Frame(master=window)
        self.frame4.pack()

        #TITOLO
        self.titolo = tk.Label(self.frame1, text ="Bancomat MolPol", background="light blue", width = 500, foreground="white", font=('Helvetica', 20), anchor= "center")
        self.titolo.pack()

        #CARICA DATASET
        self.info1 = tk.Label(self.frame2, text = "Per prima cosa è necessario caricare un Dataset:", foreground="black", font=('Helvetica', 10), anchor="center", width=500)
        self.info1.pack(side = tk.TOP)
        self.btnLoad = tk.Button(self.frame2, text="Carica Dataset", background="light blue", width=30, anchor="center")
        self.btnLoad.pack(side = tk.BOTTOM)

        #LOGIN
        self.info2 = tk.Label(self.frame3, text = "Per poter svolgere le operazioni sottostanti eseguire il login:", foreground="black", font=('Helvetica', 10), width=500)
        self.lblUser = tk.Label(self.frame3, text='Username', font=('calibre', 10, 'bold'), state="disabled")
        self.ntrUser = tk.Entry(self.frame3, font=('calibre', 10, 'normal'), state="disabled")
        self.lblPsw = tk.Label(self.frame3, text='Password', font=('calibre', 10, 'bold'), state="disabled")
        self.ntrPsw = tk.Entry(self.frame3, font=('calibre', 10, 'normal'), show='*', state="disabled")
        self.btnLogin = tk.Button(self.frame3, text="Login", state="disabled", background="light blue", width=18)
        self.info2.pack(anchor='center')
        self.lblUser.pack(anchor='center')
        self.ntrUser.pack(anchor='center')
        self.lblPsw.pack(anchor='center')
        self.ntrPsw.pack(anchor='center')
        self.btnLogin.pack(anchor='center', pady=10)

        #OPERAZIONI ESEGUIBILI DAL CLIENTE

        #VARIABILI LOGIN del cliente
        self.user = tk.StringVar()
        self.psw = tk.StringVar()

        #BINDING
        self.btnLoad.bind("<Button-1>", self.caricaDataset)
        #login
        self.btnLogin.bind("<Button-1>", self.login)

        #VARIABILI DI CONTROLLO
        self.load = False
        self.check_login = False


#FUNZIONI
#____________________________________________________________________________________________________
#1 CARICA DATASET:
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
                                self.btnLogin.config(state="normal")

                                #Cosi prende in considerazione solo il primo admin che trova
                                break
                            else:
                                messagebox.showerror("Attenzione", "Errore nel caricamento del file " + filename) 
            except IOError:
                messagebox.showerror("Attenzione", "Errore nel caricamento del file " + filename)
                return False 
            #return filename
        else:
            messagebox.showwarning("Attenzione", "Caricare il file in formato .txt")
            return False
        
    #2 LOGIN
    #-------------------------------------------------------------------------------------------------------------
    def login(self, event):
            self.user = self.ntrUser.get().strip()
            self.psw = self.ntrPsw.get().strip()
            #Se il login va a buon fine
            if self.bancomat.login(self.user, self.psw):
                messagebox.showinfo("Operazione riuscita", "Login effettuato! Adesso hai accesso alle operazioni del bancomat!")
                #Attivazione dei bottoni per le operazioni
                """ self.btnLimite.config(state="normal")
                self.btnScoperto.config(state="normal")
                self.btnDeposito.config(state="normal")
                self.btnPrelievo.config(state="normal")
                self.btnTransf.config(state="normal")"""
            else:
                messagebox.showerror("Attenzione", "Credenziali errate, controlla se sono giuste e riprova")

window = tk.Tk()
BancomatApp(window)
window.mainloop()