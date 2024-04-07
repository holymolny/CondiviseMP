from bancomat import *
from utenti import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class BancomatApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Bancomat Molpol")
        self.root.geometry("600x600")
        window.resizable(False,False)

        #self.cliccato_var = tk.BooleanVar(value=False)

        #Utilizzo di grid per posizionare il frame principale
        """self.frame = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.pack()"""


        # Creazione dei frame che suddividono la window
        self.frame1 = tk.Frame(master = window, background="light blue", width=600, height=20)
        self.frame2 = tk.Frame(master = window)
        #Frame che gestiscono il primo blocco dedicato al caricamento del file:
        self.frame3 = tk.Frame(master = window, background="light blue", width=600, height=20)
        self.frame31 = tk.Frame(master = window, background="white", width=600, height=20)
        self.frame32 = tk.Frame(master = window)
        self.frame33 = tk.Frame(master = window, background="white", width=600, height=20)
        self.frame4 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame5 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame6 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame7 = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        

        # Posizionamento dei frame all'interno della finestra principale
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame31.pack()
        self.frame32.pack()
        self.frame4.pack()
        self.frame5.pack()
        """self.frame5.grid(row=4, column=0, padx=10, pady=10)
        self.frame6.grid(row=5, column=0, padx=10, pady=10)
        self.frame6.grid(row=6, column=0, padx=10, pady=10)"""
        

        #Configuro il frame alla grandezza dell'intera finestra
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #CONFIGURAZIONE SECONDO FRAME:
        self.titolo = tk.Label(self.frame1, text ="Bancomat MolPol", background="light blue", width = 600, foreground="white", font=('Helvetica', 20), anchor= "center")
        self.titolo.pack()

        #SCRITTA sopra pulsante dataset:
        self.scritta1 = tk.Label(self.frame32, text ="Per prima cosa è necessario caricare un file:", font=('Helvetica', 12))
        self.titolo.pack()


        #CONFIGURAZIONE IV FRAME
        self.btnLoad = tk.Button(self.frame2, text="Carica Dataset", background="light blue", width=20, anchor="center")
        self.btnLoad.pack()
        self.btnLoad.focus()
        
        #Label e entry per username e password
        
        self.lblUser = tk.Label(self.frame3, text = 'Username', font=('calibre',10, 'bold'), state="disabled")
        self.ntrUser = tk.Entry(self.frame3, font=('calibre',10,'normal'), state="disabled")

        self.lblPsw = tk.Label(self.frame3, text = 'Password', font = ('calibre',10,'bold'), state="disabled")
        self.ntrPsw = tk.Entry(self.frame3, font = ('calibre',10,'normal'), show = '*', state="disabled")
        
        self.user = tk.StringVar()
        self.psw = tk.StringVar()
        self.btnLogin = tk.Button(self.frame3, text="Login", state="disabled")

        #Inserimento nel grid layout
        self.lblUser.grid(row=0,column=0)
        self.ntrUser.grid(row=0,column=1)
        self.lblPsw.grid(row=1,column=0)
        self.ntrPsw.grid(row=1,column=1)
        self.btnLogin.grid(row=2,column=1)    

        """self.lblUser.pack(side = tk.TOP)
        self.ntrUser.pack(side = tk.TOP)
        self.lblPsw.pack(side = tk.TOP)
        self.ntrPsw.pack(side = tk.TOP)"""
        #self.btnLogin.pack(side = tk.LEFT)


        #CONFIGURAZIONE TERZO FRAME
        self.btnLimite = tk.Button(self.frame4, text="Vedi limite", background="light blue", width=20, padx=10, pady=10, state="disabled")
        self.btnScoperto = tk.Button(self.frame4, text="Vedi scoperto", background="light green", width=20, padx=10, pady=10, state="disabled")
        self.btnPrelievo = tk.Button(self.frame4, text="Prelievo", background="light green", width=20, padx=10, pady=10, state="disabled")
        self.btnDeposito = tk.Button(self.frame4, text="Deposita", background="light green", width=20, padx=10, pady=10, state="disabled")
        self.btnTransf = tk.Button(self.frame4, text="Trasferisci cash", background="light green", width=20, padx=10, pady=10, state="disabled")

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
        self.lblLimite = tk.Label(self.frame5, font=('calibre',10, 'bold'), textvariable=self.limitevar)
        self.scopertovar = tk.StringVar()
        self.lblScoperto = tk.Label(self.frame5, font=('calibre',10, 'bold'), textvariable=self.scopertovar)
        
        #PRELIEVO, TRASFERIMENTO, DEPOSITO
        self.saldovar = tk.StringVar()
        self.lblSaldo = tk.Label(self.frame5, font=('calibre',10, 'bold'), textvariable=self.saldovar)
        self.lblCifraPrelievo = tk.Label(self.frame5, font=('calibre',10, 'bold'), text="Inserire somma da prelevare")
        self.ntrCifraPrelievo = tk.Entry(self.frame5, font=('calibre',10, 'bold'))
        self.btnConfermaPrelievo = tk.Button(self.frame5, text="Preleva", background="light green", width=20, padx=10, pady=10)

        self.lblCifraTransf = tk.Label(self.frame5, font=('calibre',10, 'bold'), text="Inserire somma da trasferire")
        self.ntrCifraTransf = tk.Entry(self.frame5, font=('calibre',10, 'bold'))

        self.lblUserTransf = tk.Label(self.frame5, font=('calibre',10, 'bold'), text="Inserire username destinatario")
        self.ntrUserTransf = tk.Entry(self.frame5, font=('calibre',10, 'bold'))
        self.btnConfermaTransf = tk.Button(self.frame5, text="Invia denaro", background="light green", width=20, padx=10, pady=10)

        self.lblCifraDeposito = tk.Label(self.frame5, font=('calibre',10, 'bold'), text="Inserire somma da depositare")
        self.ntrCifraDeposito = tk.Entry(self.frame5, font=('calibre',10, 'bold'))
        self.btnConfermaDeposito = tk.Button(self.frame5, text="Deposita", background="light green", width=20, padx=10, pady=10)
        
        #MOSTRA LIMITE E SCOPERTO
        self.lblLimite.pack_forget()
        self.lblScoperto.pack_forget()

        #PRELIEVO
        self.lblSaldo.pack_forget()
        self.lblCifraPrelievo.pack_forget()
        self.ntrCifraPrelievo.pack_forget()
        self.btnConfermaPrelievo.pack_forget()

        #DEPOSITO
        self.lblCifraDeposito.pack_forget()
        self.ntrCifraDeposito.pack_forget()
        self.btnConfermaDeposito.pack_forget()

        #TRASFERIMENTO
        self.lblCifraTransf.pack_forget()
        self.ntrCifraTransf.pack_forget()
        self.lblUserTransf.pack_forget()
        self.ntrUserTransf.pack_forget()
        self.btnConfermaTransf.pack_forget()



        #BINDING
        #Caricamento del file da cui caricare il bancomat 
        self.btnLoad.bind("<Button-1>", self.caricaDataset)
        #Attivazione dei button delle operazioni eseguibili
        self.btnLimite.bind("<Button-1>", self.mostraLimite)
        self.btnScoperto.bind("<Button-1>", self.mostraScoperto)
        self.btnPrelievo.bind("<Button-1>", self.attivaPrelievo)
        self.btnDeposito.bind("<Button-1>", self.attivaDeposito)
        self.btnTransf.bind("<Button-1>", self.attivaTransf)
        #Conferma login
        self.btnLogin.bind("<Button-1>", self.login)
        #Conferma delle operazioni
        self.btnConfermaPrelievo.bind("<Button-1>", self.confermaPrelievo)
        self.btnConfermaDeposito.bind("<Button-1>", self.confermaDeposito)
        self.btnConfermaTransf.bind("<Button-1>", self.confermaTransf)
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
            self.filename = filename
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
        

    def disabilitaOperazioni(self):
        #Azzero le variabili di login
        self.user = tk.StringVar()
        self.psw = tk.StringVar()
        #Cancella i valori delle entry di Login
        #Elimina tutto il contenuto della entry
        self.ntrUser.delete(0, tk.END)
        self.ntrPsw.delete(0, tk.END)

        #Disabilita i button
        self.btnLimite.config(state="disabled")
        self.btnScoperto.config(state="disabled")
        self.btnDeposito.config(state="disabled")
        self.btnPrelievo.config(state="disabled")
        self.btnTransf.config(state="disabled")


    def login(self, event):
        self.user = self.ntrUser.get().strip()
        self.psw = self.ntrPsw.get().strip()
        #Se il login va a buon fine
        if self.bancomat.login(self.user, self.psw):
            messagebox.showinfo("Operazione riuscita", "Login effettuato! Adesso hai accesso alle operazioni del bancomat!")
            #Attivazione dei bottoni per le operazioni
            self.btnLimite.config(state="normal")
            self.btnScoperto.config(state="normal")
            self.btnDeposito.config(state="normal")
            self.btnPrelievo.config(state="normal")
            self.btnTransf.config(state="normal")
        else:
            messagebox.showerror("Attenzione", "Credenziali errate, controlla se sono giuste e riprova")



    def mostraLimite(self, event):
        #Attivazione dei campi per effettuare il login
        if self.bancomat.get_limite_prelievo(self.user, self.psw):
            #Rendo invisibili gli altri widget che eventualmente potrebbero essere aperti
            self.lblScoperto.pack_forget()
            self.lblSaldo.pack_forget()
            self.lblCifraPrelievo.pack_forget()
            self.ntrCifraPrelievo.pack_forget()
            self.btnConfermaPrelievo.pack_forget()
            #Aggiungere qui sotto quelli ancora da creare

            #Rendo visibile solo quello che mostra il limite di prelievo
            self.lblLimite.pack(side = tk.TOP)
            self.limitevar.set("Limite prelievo = " + str(self.bancomat.get_limite_prelievo(self.user, self.psw)))
        else:
            messagebox.showerror("Errore", "Ops, qualcosa è andato storto. Controlla le credenziali e riprova.")

    def mostraScoperto(self, event):
        if self.bancomat.get_scoperto_massimo(self.user, self.psw):
            #Rendo invisibili gli altri widget che eventualmente potrebbero essere aperti
            self.lblLimite.pack_forget()
            self.lblSaldo.pack_forget()
            self.lblCifraPrelievo.pack_forget()
            self.ntrCifraPrelievo.pack_forget()
            self.btnConfermaPrelievo.pack_forget()
            #Aggiungere qui sotto quelli ancora da creare

            #Rendo visibile solo quello che mostra lo scoperto
            self.lblScoperto.pack(side = tk.TOP)
            self.scopertovar.set("Lo scoperto massimo è: " + str(self.bancomat.get_scoperto_massimo(self.user, self.psw)))
        else:
            messagebox.showerror("Errore", "Ops, qualcosa è andato storto. Controlla le credenziali e riprova.")

    def attivaPrelievo(self, event):
        #Rendo visibile i campi per fare il prelievo
        risultato = self.bancomat.get_saldo(self.user, self.psw)
        if risultato == "Utente non valido":
            messagebox.showerror("Errore", risultato + "\nNon sei abilitato per completare questa operazione.")
        else:
            self.lblSaldo.pack(side = tk.TOP)
            self.saldovar.set("Saldo disponibile: " + str(self.bancomat.get_saldo(self.user, self.psw)))
            
            self.lblCifraPrelievo.pack(side = tk.TOP)
            self.ntrCifraPrelievo.pack(side = tk.TOP)
            self.btnConfermaPrelievo.pack(side = tk.TOP)

        
        #Rendo invisibili gli altri widget che eventualmente potrebbero essere aperti
        self.lblLimite.pack_forget()
        self.lblScoperto.pack_forget()
        self.lblCifraDeposito.pack_forget()
        self.ntrCifraDeposito.pack_forget()
        self.btnConfermaDeposito.pack_forget()
        self.lblCifraTransf.pack_forget()
        self.ntrCifraTransf.pack_forget()
        self.lblUserTransf.pack_forget()
        self.ntrUserTransf.pack_forget()
        self.btnConfermaTransf.pack_forget()
        #Aggiungere qui sotto quelli ancora da creare


    def confermaPrelievo(self, event):
        somma = self.ntrCifraPrelievo.get()
        if somma.strip().isdigit():
            somma = int(somma)
            risposta = messagebox.askquestion("Conferma", "Vuoi procedere con l'operazione?")
            if risposta:
                esito, msg = self.bancomat.preleva(self.user, self.psw, somma)
                if esito:
                    self.bancomat.salva_su_file(self.userAdmin, self.pswAdmin, self.filename)
                    self.root.after(250, 
                                    lambda: messagebox.showinfo("Operazione riuscita", "Denaro prelevato con successo!\nPer svolgere altre operazioni effettuare il login di nuovo."))
                    #Nascondo i widget dell'operazione in corso
                    self.lblSaldo.pack_forget()
                    self.lblCifraPrelievo.pack_forget()
                    self.ntrCifraPrelievo.pack_forget()
                    self.btnConfermaPrelievo.pack_forget()
                    #Richiamo la funzione che cancella i valori nel login e disabilita i button
                    self.disabilitaOperazioni()
                else:
                    messagebox.showwarning("Attenzione", msg)
        else:
            messagebox.showerror("Errore", "Ops, qualcosa è andato storto. Controlla la cifra inserita e riprova.")
    
    
    def attivaTransf(self, event):
        risultato = self.bancomat.get_saldo(self.user, self.psw)
        if risultato == "Utente non valido":
            messagebox.showerror("Errore", risultato + "\nNon sei abilitato per completare questa operazione.")
        else:
            self.lblSaldo.pack(side = tk.TOP)
            self.saldovar.set("Saldo disponibile: " + str(self.bancomat.get_saldo(self.user, self.psw)))
            if self.bancomat.get_saldo(self.user, self.psw):
                self.lblSaldo.pack(side = tk.TOP)
                self.saldovar.set("Saldo disponibile: " + str(self.bancomat.get_saldo(self.user, self.psw)))
            self.lblCifraTransf.pack(side = tk.TOP)
            self.ntrCifraTransf.pack(side = tk.TOP)
            self.lblUserTransf.pack(side = tk.TOP)
            self.ntrUserTransf.pack(side = tk.TOP)
            self.btnConfermaTransf.pack(side = tk.TOP)

            #Rendo invisibili gli altri widget che eventualmente potrebbero essere aperti
        self.lblLimite.pack_forget()
        self.lblScoperto.pack_forget()
        self.lblCifraDeposito.pack_forget()
        self.ntrCifraDeposito.pack_forget()
        self.btnConfermaDeposito.pack_forget()
        self.lblCifraPrelievo.pack_forget()
        self.ntrCifraPrelievo.pack_forget()
        self.btnConfermaPrelievo.pack_forget()
        #Aggiungere qui sotto quelli ancora da creare

    def confermaTransf(self, event):
        somma = self.ntrCifraTransf.get()
        dest = self.ntrUserTransf.get()
        if somma.strip().isdigit():
            somma = int(somma)
            risposta = messagebox.askquestion("Conferma", "Vuoi procedere con l'operazione?")
            if risposta:
                esito, msg = self.bancomat.trasferisci(self.user, self.psw, dest, somma)
                if esito:
                    self.bancomat.salva_su_file(self.userAdmin, self.pswAdmin, self.filename)
                    self.root.after(250, 
                                    lambda: messagebox.showinfo("Operazione riuscita", "Denaro trasferito sul conto di " + dest +"\nPer svolgere altre operazioni effettuare il login di nuovo."))
                    #Nascondo i widget dell'operazione in corso
                    self.lblSaldo.pack_forget()                    
                    self.lblCifraTransf.pack_forget()
                    self.ntrCifraTransf.pack_forget()
                    self.lblUserTransf.pack_forget()
                    self.ntrUserTransf.pack_forget()
                    self.btnConfermaTransf.pack_forget()
                    #Richiamo la funzione che cancella i valori nel login e disabilita i button
                    self.disabilitaOperazioni()
                else:
                    messagebox.showwarning("Attenzione", msg)
        else:
            messagebox.showerror("Errore", "Ops, qualcosa è andato storto. Controlla la cifra inserita e lo username del destinatario e riprova.")
    

    def attivaDeposito(self, event):
        risultato = self.bancomat.get_saldo(self.user, self.psw)
        if risultato == "Utente non valido":
            messagebox.showerror("Errore", risultato + "\nNon sei abilitato per completare questa operazione.")
        else:
            self.lblSaldo.pack(side = tk.TOP)
            self.saldovar.set("Saldo disponibile: " + str(self.bancomat.get_saldo(self.user, self.psw)))
            self.lblCifraDeposito.pack(side = tk.TOP)
            self.ntrCifraDeposito.pack(side = tk.TOP)
            self.btnConfermaDeposito.pack(side = tk.TOP)

        #Rendo invisibili gli altri widget che eventualmente potrebbero essere aperti
        self.lblLimite.pack_forget()
        self.lblScoperto.pack_forget()
        self.lblCifraPrelievo.pack_forget()
        self.ntrCifraPrelievo.pack_forget()
        self.btnConfermaPrelievo.pack_forget()
        self.lblCifraTransf.pack_forget()
        self.ntrCifraTransf.pack_forget()
        self.lblUserTransf.pack_forget()
        self.ntrUserTransf.pack_forget()
        self.btnConfermaTransf.pack_forget()
        #Aggiungere qui sotto quelli ancora da creare
   
    def confermaDeposito(self, event): 
        somma = self.ntrCifraDeposito.get()
        if somma.strip().isdigit():
            somma = int(self.ntrCifraDeposito.get())
            risposta = messagebox.askquestion("Conferma", "Vuoi procedere con l'operazione?")
            if risposta:
                esito, msg = self.bancomat.deposita(self.user, self.psw, somma)
                if esito:
                    self.bancomat.salva_su_file(self.userAdmin, self.pswAdmin, self.filename)
                    self.root.after(250, 
                                    lambda: messagebox.showinfo("Operazione riuscita", "Denaro depositato con successo!\nPer svolgere altre operazioni effettuare il login di nuovo."))
                    #Nascondo i widget dell'operazione in corso
                    self.lblSaldo.pack_forget()
                    self.lblCifraDeposito.pack_forget()
                    self.ntrCifraDeposito.pack_forget()
                    self.btnConfermaDeposito.pack_forget()
                    #Richiamo la funzione che cancella i valori nel login e disabilita i button
                    self.disabilitaOperazioni()
                else:
                    messagebox.showwarning("Attenzione", msg)
        else:
            messagebox.showerror("Errore", "Ops, qualcosa è andato storto. Controlla la cifra inserita e riprova.")

window = tk.Tk()
BancomatApp(window)
window.mainloop()