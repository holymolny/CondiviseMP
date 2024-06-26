"""L’interfaccia grafica deve essere implementata nel file gui.py. All’avvio dell’interfaccia
grafica, deve essere caricato il file bancomat.txt generato dall’esecuzione dei test
automatici del file main.py. Successivamente, deve essere simulata una sessione
allo sportello bancomat nell’ordine:

1. deve essere richiesto il login dell’utente;
2. deve essere richiesta quale operazione vuole essere effettuata fra prelievo,
deposito e trasferimento ad altro conto corrente;
3. devono essere richieste le informazioni per svolgere l’operazione;
4. in caso di errori, a schermo devono essere mostrati i messaggi di errore
definiti nella classe Bancomat;
5. in caso di successo, deve essere mostrato un messaggio di riuscita dell’operazione
e salvare su file il nuovo stato del Bancomat;
6. dopo alcuni secondi, deve essere richiesto il login per ripartire dal punto (1).

L’aspetto generale dell’interfaccia grafica `e lasciato alla creativit`a dello studente.
"""
from bancomat import *
from utenti import *
import tkinter as tk
#mi serve per generare i messaggi
from tkinter import messagebox
#mi serve per caricare file dal pc 
from tkinter import filedialog

class BancomatApp():
    #Costruttore
    def __init__(self, root):
        self.root = root
        self.root.title("Bancomat Molpol")
        self.root.geometry("500x600")
        window.resizable(False,False)
    
    #GESTIONE FRAME
        self.frame1 = tk.Frame(master = window)
        self.frame1.pack()
        #FRAME CARICA-DATASET
        self.frame2 = tk.Frame(master=window)
        self.frame2.pack()
        #FRAME LOGIN
        self.frame3 = tk.Frame(master=window)
        self.frame3.pack()
        #FRAME BOTTONI-OPERAZIONI
        self.frame4 = tk.Frame(master=window)
        self.frame4.pack()
        #FRAME CREDITS
        self.frame5 = tk.Frame(master = window)
        self.frame5.pack()
      
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

        #VARIABILI LOGIN del cliente
        self.user = tk.StringVar()
        self.psw = tk.StringVar()

        #OPERAZIONI ESEGUIBILI DAL CLIENTE
        self.info3 = tk.Label(self.frame4, text= "Scegliere una delle seguenti operazioni:", foreground="black", font=('Helvetica', 10), width=500)
        self.btnLimite = tk.Button(self.frame4, text="Limite Prelievo", background="light blue", width=20, pady=5, state="disabled")
        self.btnScoperto = tk.Button(self.frame4, text="Scoperto", background="light blue", width=20, pady=5, state="disabled")
        self.btnPrelievo = tk.Button(self.frame4, text="Prelievo", background="light blue", width=20, pady=5, state="disabled")
        self.btnDeposito = tk.Button(self.frame4, text="Deposita", background="light blue", width=20, pady=5, state="disabled")
        self.btnTransf = tk.Button(self.frame4, text="Trasferisci cash", background="light blue", width=20, pady=5, state="disabled")
        self.info3.pack(anchor= "center")
        self.btnLimite.pack(anchor= "center")
        self.btnScoperto.pack(anchor= "center")
        self.btnPrelievo.pack(anchor= "center")
        self.btnDeposito.pack(anchor= "center")
        self.btnTransf.pack(anchor= "center")

        #LIMITE E SCOPERTO
        self.limitevar = tk.StringVar()
        self.lblLimite = tk.Label(self.frame4, font=('calibre',10, 'bold'), textvariable=self.limitevar, pady = 10, foreground="green")
        self.scopertovar = tk.StringVar()
        self.lblScoperto = tk.Label(self.frame4, font=('calibre',10, 'bold'), textvariable=self.scopertovar, pady=10, foreground="green")
        #MOSTRA LIMITE E SCOPERTO
        self.lblLimite.pack_forget()
        self.lblScoperto.pack_forget()

        #PRELIEVO, TRASFERIMENTO, DEPOSITO
        self.saldovar = tk.StringVar()
        self.lblSaldo = tk.Label(self.frame4, font=('calibre',10, 'bold'), textvariable=self.saldovar, pady=10, foreground="green")
        #prelievo
        self.lblCifraPrelievo = tk.Label(self.frame4, font=('calibre',10, 'bold'), text="Inserire somma da prelevare")
        self.ntrCifraPrelievo = tk.Entry(self.frame4, font=('calibre',10, 'bold'))
        self.btnConfermaPrelievo = tk.Button(self.frame4, text="Preleva", background="green", foreground="white", width=19, pady=10)
        #trasferimento
        self.lblCifraTransf = tk.Label(self.frame4, font=('calibre',10, 'bold'), text="Inserire somma da trasferire")
        self.ntrCifraTransf = tk.Entry(self.frame4, font=('calibre',10, 'bold'))
        self.lblUserTransf = tk.Label(self.frame4, font=('calibre',10, 'bold'), text="Inserire username destinatario")
        self.ntrUserTransf = tk.Entry(self.frame4, font=('calibre',10, 'bold'))
        self.btnConfermaTransf = tk.Button(self.frame4, text="Invia denaro", background="green", foreground="white", width=19, pady=10)
        self.btnConfermaTransf.pack(anchor="center")
        #deposito
        self.lblCifraDeposito = tk.Label(self.frame4, font=('calibre',10, 'bold'), text="Inserire somma da depositare")
        self.ntrCifraDeposito = tk.Entry(self.frame4, font=('calibre',10, 'bold'))
        self.btnConfermaDeposito = tk.Button(self.frame4, text="Deposita", background="green", foreground="white", width=19, pady=10)
        self.btnConfermaDeposito.pack(anchor="center")
        #LOGOUT
        self.btnLogout = tk.Button(self.frame3, text="Esci", background="red", foreground="white", width=18, pady=10)
        self.btnLogout.pack(anchor="center")
        
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
        #LOGOUT
        self.btnLogout.pack_forget()

        #BINDING
        self.btnLoad.bind("<Button-1>", self.caricaDataset)
        #login
        self.btnLogin.bind("<Button-1>", self.login)
        #mostralimite e scoperto
        self.btnLimite.bind("<Button-1>", self.mostraLimite)
        self.btnScoperto.bind("<Button-1>", self.mostraScoperto)
        #prelievo, deposito e trasferimento
        self.btnPrelievo.bind("<Button-1>", self.attivaPrelievo)
        self.btnDeposito.bind("<Button-1>", self.attivaDeposito)
        self.btnTransf.bind("<Button-1>", self.attivaTransf)
        #conferma
        self.btnConfermaPrelievo.bind("<Button-1>", self.confermaPrelievo)
        self.btnConfermaDeposito.bind("<Button-1>", self.confermaDeposito)
        self.btnConfermaTransf.bind("<Button-1>", self.confermaTransf)
        #Uscita
        self.btnLogout.bind("<Button-1>", self.logout)

        #CREDITS
        self.info5 = tk.Label(self.frame5, text="______________________________________\n\nMihnea Sever Molnar, 579590\n Irene Poli, 604855\n Programmazione e Analisi Dati - ModA, a.a. 2023-2024\n______________________________________", foreground="black", font=('calibre',10, 'bold'), width=500, height=20)
        self.info5.pack()

#FUNZIONI
#____________________________________________________________________________________________________
#1 CARICA DATASET:
    def caricaDataset(self, event):
        #Carica il file:
        filePath = filedialog.askopenfilename()
        filePath = filePath.strip() #elimina eventuali spazi bianchi a inizio e fine stringa
        indiceBarra = filePath.rfind("/") #restituisce l'ultimo indice di "/"
        filename = filePath[indiceBarra + 1:]
        indicePunto = filename.rfind(".") #restituisce l'ultimo indice di "."
        estensione = filename[indicePunto + 1:]
        #verifico che estensione sia txt e che quindi il file che sto caricando sia di tipo .txt
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
                            #oggetto istanza della classe bancomat, ricordiamo che bancomat richiede tre argomenti di cui il primo è l'oggetto ADMIN
                            self.bancomat = Bancomat(Admin(self.userAdmin, self.pswAdmin), 0, 0)
                            #carica
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
            #prendo ciò che viene inserito nella entry ed elimino eventuali spazi
            self.user = self.ntrUser.get().strip()
            self.psw = self.ntrPsw.get().strip()
            #Se il login va a buon fine
            loggato = self.bancomat.login(self.user, self.psw)
            if loggato:
                messagebox.showinfo("Operazione riuscita", "Login effettuato! Adesso hai accesso alle operazioni del bancomat!")
                #Attivazione dei bottoni per le operazioni
                self.btnLimite.config(state="normal")
                self.btnScoperto.config(state="normal")
                self.btnDeposito.config(state="normal")
                self.btnPrelievo.config(state="normal")
                self.btnTransf.config(state="normal")

                #Disattivo il login - perchè al posto dei widget per effettuare il login appare il bottone "Esci"
                self.btnLogout.pack(anchor="center")
                self.btnLogin.pack_forget()
                self.lblUser.pack_forget()
                self.ntrUser.pack_forget()
                self.lblPsw.pack_forget()
                self.ntrPsw.pack_forget()
            else:
                messagebox.showerror("Attenzione", "Credenziali errate, controlla se sono giuste e riprova")

#3 DISABILITA OPERAZIONI:
#________________________________________________________________________________________________________________________
    def disabilitaOperazioni(self):
        #Azzero le variabili di login
        self.user = tk.StringVar()
        self.psw = tk.StringVar()

        #Cancella i valori delle entry di Login
        #Elimina tutto il contenuto della entry
        self.ntrUser.delete(0, tk.END)
        self.ntrPsw.delete(0, tk.END)
        self.ntrCifraPrelievo.delete(0, tk.END)
        self.ntrCifraDeposito.delete(0, tk.END)
        self.ntrCifraTransf.delete(0, tk.END)
        self.ntrUserTransf.delete(0, tk.END)
        
        #Disabilita i button
        self.btnLimite.config(state="disabled")
        self.btnScoperto.config(state="disabled")
        self.btnDeposito.config(state="disabled")
        self.btnPrelievo.config(state="disabled")
        self.btnTransf.config(state="disabled")

        #Mostra tutti i campi del login
        self.lblUser.pack()
        self.ntrUser.pack()
        self.lblPsw.pack()
        self.ntrPsw.pack()
        self.btnLogin.pack()

        #Nasconde tutti gli altri widget
        self.lblLimite.pack_forget()
        self.lblScoperto.pack_forget()
        self.lblSaldo.pack_forget()
        self.lblCifraPrelievo.pack_forget()
        self.ntrCifraPrelievo.pack_forget()
        self.btnConfermaPrelievo.pack_forget()
        self.lblCifraDeposito.pack_forget()
        self.ntrCifraDeposito.pack_forget()
        self.btnConfermaDeposito.pack_forget()
        self.lblCifraTransf.pack_forget()
        self.ntrCifraTransf.pack_forget()
        self.lblUserTransf.pack_forget()
        self.ntrUserTransf.pack_forget()
        self.btnConfermaTransf.pack_forget()
        #Nasconde il button di logout
        self.btnLogout.pack_forget()

#4 MOSTRA LIMITE E SCOPERTO
#________________________________________________________________________________________________________________________
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

#5 PRIELIEVO:
#________________________________________________________________________________________________________________________

    def attivaPrelievo(self, event):
        #Rendo visibilo i campi per fare il prelievo e mi ricavo il saldo
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
       
    def confermaPrelievo(self, event):
        #mi ricavo la quantità di denaro dalla entry
        somma = self.ntrCifraPrelievo.get()
        if somma.strip().isdigit(): #la stringa deve essere composta da soli numeri
            somma = int(somma)
            #conferma dell'operazione
            risposta = messagebox.askquestion("Conferma", "Vuoi procedere con l'operazione?") #booleano
            if risposta:
                #ho due variabili perchè la funzione preleva ha due return! (Ture, "") in caso positivo o (False, messaggio) in caso negativo. 
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
    
#6 TRASFERIMENTO:
#________________________________________________________________________________________________________________________

    def attivaTransf(self, event):
        #mi ricavo il saldo
        risultato = self.bancomat.get_saldo(self.user, self.psw)
        if risultato == "Utente non valido":
            messagebox.showerror("Errore", risultato + "\nNon sei abilitato per completare questa operazione.")
        else:
            #mostro a schermo le seguenti cose:
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
       
    def confermaTransf(self, event):
        #dati che mi ricavo dalle entry 
        somma = self.ntrCifraTransf.get()
        dest = self.ntrUserTransf.get()
        if somma.strip().isdigit():
            somma = int(somma)
            risposta = messagebox.askquestion("Conferma", "Vuoi procedere con l'operazione?")
            if risposta:
                #anche qui l'output della funzione trasferisci returna due elementi
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
#7 DEPOSITO:
#________________________________________________________________________________________________________________________

    def attivaDeposito(self, event):
        #mi ricavo il saldo
        risultato = self.bancomat.get_saldo(self.user, self.psw)
        if risultato == "Utente non valido":
            messagebox.showerror("Errore", risultato + "\nNon sei abilitato per completare questa operazione.")
        else:
            #mostro a schermo:
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
      
   
    def confermaDeposito(self, event): 
        #mi ricavo dalla entry la quantità di denaro da depositare
        somma = self.ntrCifraDeposito.get()
        if somma.strip().isdigit():
            somma = int(self.ntrCifraDeposito.get())
            risposta = messagebox.askquestion("Conferma", "Vuoi procedere con l'operazione?")
            if risposta:
                #deposita returna due elementi
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



    def logout(self, event):
        #Disabilita le operazioni
        self.disabilitaOperazioni()


window = tk.Tk()
BancomatApp(window)
window.mainloop()