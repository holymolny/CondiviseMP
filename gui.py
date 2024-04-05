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
from tkinter import messagebox
from tkinter import filedialog

class BancomatApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Bancomat Molpol")
        self.root.geometry("600x850")
        window.resizable(False,False)
        root.configure(background="white")
    
    # Creazione dei frame che suddividono la window
        self.frame1 = tk.Frame(master = window, background="light blue", width=600, height=20)
        self.frame2 = tk.Frame(master = window)
        self.frame3 = tk.Frame(master = window, background="light blue", width=600, height=20)
        self.frame4 = tk.Frame(master = window, background="white", width=600, height=20)
        self.frame5 = tk.Frame(master = window)
        self.frame6 = tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame7 = tk.Frame(master=window)
        self.frame8 = tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame9 = tk.Frame(master=window)
        self.frame10 = tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame11 = tk.Frame(master=window)
        self.frame12 = tk.Frame(master=window)
        self.frame13 = tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame14 = tk.Frame(master=window)
        self.frame15 = tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame16 = tk.Frame(master=window)
        self.frame17 = tk.Frame(master=window)
        self.frame18 = tk.Frame(master = window, background="white", width= 600, height= 5)
        self.frame19 = tk.Frame(master=window)
        self.frame20 = tk.Frame(master=window)
        self.frame21 = tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame22 = tk.Frame(master=window)
        self.frame23 = tk.Frame(master=window)
        self.frame24 = tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame25 = tk.Frame(master=window)
        self.frame26 = tk.Frame(master=window)
        self.frame27 = tk.Frame(master=window)
        self.frame28 = tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame29 = tk.Frame(master=window)
        self.frame30 = tk.Frame(master=window)
        self.frame31 = tk.Frame(master=window)
        self.frame32 = tk.Frame(master=window)
        self.frame33 = tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame34 = tk.Frame(master=window)
        self.frame35 =tk.Frame(master = window, background="white", width= 600, height= 10)
        self.frame36 = tk.Frame(master = window, background="light blue", width=600, height=80)
    # Posizionamento dei frame all'interno della finestra principale
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()
        self.frame9.pack()
        self.frame10.pack()
        self.frame11.pack()
        self.frame12.pack()
        self.frame13.pack()
        self.frame14.pack()
        self.frame15.pack()
        self.frame16.pack()
        self.frame17.pack()
        self.frame18.pack()
        self.frame19.pack()
        self.frame20.pack()
        self.frame21.pack()
        self.frame22.pack()
        self.frame23.pack()
        self.frame24.pack()
        self.frame25.pack() 
        self.frame26.pack()
        self.frame27.pack()
        self.frame28.pack()
        self.frame29.pack() 
        self.frame30.pack()
        self.frame31.pack()  
        self.frame32.pack()
        self.frame33.pack() 
        self.frame34.pack() 
        self.frame35.pack()
        self.frame36.pack()
    
        #TITOLO
        self.titolo = tk.Label(
            self.frame2,
            text ="Bancomat MolPol",
            background="light blue",
            width = 600,
            foreground="white",
            font=('Helvetica', 20),
            anchor= "center"
            )
        self.titolo.pack()

        #TESTO PRIMA DI CARICA DATASET
        self.testo1 = tk.Label(self.frame5, text="Selezionare un file.txt da caricare:", background="white", font=('Helvetica', 10))
        self.testo1.pack()

        #BOTTONE CARICA DATASET
        self.btnLoad = tk.Button(self.frame7, text="Carica Dataset", background="light blue", width=20, anchor="center")
        self.btnLoad.pack()

        #AREA AUTENTICAZIONE
        #----------------------------------------------------------------------------------------------------------------
        self.testo2 = tk.Label(self.frame9, text="Prima di eseguire ogni operazione è necessario inserire username e password:", background="white", font=('Helvetica', 10))
        self.testo2.pack()
        #area username
        self.lblUser = tk.Label(self.frame11, text='Username', font=('calibre', 10, 'bold'), state="disabled")
        self.lblUser.grid(row=0, column=0, padx=5, pady=5)
        self.ntrUser = tk.Entry(self.frame11, font=('calibre', 10, 'normal'), state="disabled")
        self.ntrUser.grid(row=0, column=1, padx=5, pady=5)
        #area password
        self.lblPsw = tk.Label(self.frame12, text='Password', font=('calibre', 10, 'bold'), state="disabled")
        self.lblPsw.grid(row=0, column=0, padx=5, pady=5)
        self.ntrPsw = tk.Entry(self.frame12, font=('calibre', 10, 'normal'), state="disabled", show="*")
        self.ntrPsw.grid(row=0, column=1, padx=5, pady=5)
        #-----------------------------------------------------------------------------------------------------------------
        #AREA BOTTONI 
        #-----------------------------------------------------------------------------------------------------------------
        self.testo3 = tk.Label(self.frame14, text="Selezionare l'operazione che si desidera eseguire", background="white", font=('Helvetica', 10))
        self.testo3.pack()
        #BOTTONI INFO
        self.btnLimite = tk.Button(self.frame19, text="Vedi limite", background="light blue", width=20, padx=10, pady=10, state="disabled")
        self.btnScoperto = tk.Button(self.frame20, text="Vedi scoperto", background="light blue", width=20, padx=10, pady=10, state="disabled")
        self.btnLimite.pack()
        self.btnScoperto.pack()
        #BOTTONI PRELIEVO - DEPOSITA - TRASFERISCI:
        self.btnPrelievo = tk.Button(self.frame25, text="Prelievo", background="light blue", width=20, padx=10, pady=10, state="disabled")
        self.btnDeposito = tk.Button(self.frame29, text="Deposita", background="light blue", width=20, padx=10, pady=10, state="disabled")
        self.btnTransf = tk.Button(self.frame34, text="Trasferisci", background="light blue", width=20, padx=10, pady=10, state="disabled")
        self.btnDeposito.pack()
        self.btnPrelievo.pack()
        self.btnTransf.pack()
       

        #RISULTATI DEI PRIMI DUE BOTTONI (LIMITE E SCOPERTO) - STAMPA:
        self.limitevar = tk.StringVar()
        self.lblLimite = tk.Label(self.frame16, font=('calibre',10, 'bold'), textvariable=self.limitevar)
        self.scopertovar = tk.StringVar()
        self.lblScoperto = tk.Label(self.frame17, font=('calibre',10, 'bold'), textvariable=self.scopertovar)

        #MOSTRA LIMITE E SCOPERTO
        self.lblLimite.pack_forget()
        self.lblScoperto.pack_forget()

        #AREA PRELIEVO-DEPOSITA-TRASFERISCI:
        #Label Prelievo:
        self.testo4 = tk.Label(self.frame22, text="Inserire la quantità di denaro che si desidera prelevare:", background="white", font=('Helvetica', 10))
        self.testo4.pack()
        self.lblCifraPrelievo = tk.Label(self.frame23, text='Somma:', font=('calibre', 10, 'bold'), state="disabled")
        self.lblCifraPrelievo.grid(row=0, column=0, padx=5, pady=5)
        self.ntrCifraPrelievo = tk.Entry(self.frame23, font=('calibre', 10, 'normal'), state="disabled")
        self.ntrCifraPrelievo.grid(row=0, column=1, padx=5, pady=5)
        #Label Deposita
        self.testo5 = tk.Label(self.frame26, text="Inserire la quantità di denaro che si desidera depositare:", background="white", font=('Helvetica', 10))
        self.testo5.pack()
        self.lblCifraDeposito = tk.Label(self.frame27, text='Somma:', font=('calibre', 10, 'bold'), state="disabled")
        self.lblCifraDeposito.grid(row=0, column=0, padx=5, pady=5)
        self.ntrCifraDeposito = tk.Entry(self.frame27, font=('calibre', 10, 'normal'), state="disabled")
        self.ntrCifraDeposito.grid(row=0, column=1, padx=5, pady=5)

        #Label Trasferisci
        self.testo6 = tk.Label(self.frame30, text="Inserire la quantità di denaro che si vuole trasferire e destinatario:", background="white", font=('Helvetica', 10))
        self.testo6.pack()

        self.lblCifraTrasfSomma = tk.Label(self.frame31, text='Somma:', font=('calibre', 10, 'bold'), state="disabled")
        self.lblCifraTrasfSomma.grid(row=0, column=0, padx=5, pady=5)
        self.ntrCifraTrasfSomma = tk.Entry(self.frame31, font=('calibre', 10, 'normal'), state="disabled")
        self.ntrCifraTrasfSomma.grid(row=0, column=1, padx=5, pady=5)
        self.lblTrasfDest = tk.Label(self.frame32, text='Destinatario:', font=('calibre', 10, 'bold'), state="disabled")
        self.lblTrasfDest.grid(row=0, column=0, padx=5, pady=5)
        self.ntrTrasfDest = tk.Entry(self.frame32, font=('calibre', 10, 'normal'), state="disabled")
        self.ntrTrasfDest.grid(row=0, column=1, padx=5, pady=5)

        #PRELIEVO
        #self.lblSaldo.pack_forget() <----------------- SU QUESTO DA ERRORE
        self.lblCifraPrelievo.pack_forget()
        self.ntrCifraPrelievo.pack_forget()

        #DISCORSO SALDO
        self.saldovar = tk.StringVar()
        #self.lblSaldo = tk.Label(self.frameX, font=('calibre',10, 'bold'), textvariable=self.saldovar) <------- ANCHE QUI PERCHE' C'è DA DECIDERE UN FRAME

        #BINDING
        self.btnLoad.bind("<Button-1>", self.caricaDataset)
        self.btnLimite.bind("<Button-1>", self.mostraLimite)
        self.btnScoperto.bind("<Button-1>", self.mostraScoperto)
        self.btnPrelievo.bind("<Button-1>", self.prelievo)
        self.btnDeposito.bind("<Button-1>", self.deposita)
        self.btnTransf.bind("<Button-1>", self.trasferisci)

        #VARIABILI DI CONTROLLO
        self.load = False
        self.check_login = False

#------------------------------------------------------------------------------------------------------------------------------------------------
#FUNZIONI:

#1 FUNZIONE CHE CARICA IL DATASET
#----------------------------------------------------------------------------------------------
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

                            #?????????
                            self.btnLimite.config(state="normal")
                            self.btnScoperto.config(state="normal")
                            """self.btnDeposito.config(state="normal")
                            self.btnPrelievo.config(state="normal")
                            self.btnTransf.config(state="normal")"""
            except IOError:
                messagebox.showerror("Attenzione", "Errore nel caricamento del file " + filename)
                return False 
            #return filename
        else:
            messagebox.showwarning("Attenzione", "Caricare il file in formato .txt")
            return False

    #2 - FUNZIONE CHE MOSTRA IL LIMITE DEL DENARO PRELEVABILE
    #--------------------------------------------------------
    def mostraLimite(self, event):
        #Attivazione dei campi per effettuare il login
        user = self.ntrUser.get().strip()
        psw = self.ntrPsw.get().strip()
        if self.bancomat.get_limite_prelievo(user, psw):
            self.lblLimite.pack(side = tk.TOP)
            self.limitevar.set("Limite prelievo = " + str(self.bancomat.get_limite_prelievo(user, psw)))
        else:
            messagebox.showerror("Attenzione", "Credenziali errate, controlla se sono giuste e riprova")

    #3 - FUNZIONE CHE MOSTRA LO SCOPERTO MASSIMO
    #------------------------------------------------------
    def mostraScoperto(self, event):
        user = self.ntrUser.get().strip()
        psw = self.ntrPsw.get().strip()
        if self.bancomat.get_scoperto_massimo(user, psw):
            self.lblScoperto.pack(side = tk.TOP)
            self.scopertovar.set("Lo scoperto massimo è: " + str(self.bancomat.get_scoperto_massimo(user, psw)))
        else:
            messagebox.showerror("Attenzione", "Credenziali errate, controlla se sono giuste e riprova")

   
    def prelievo(self, event):
        user = self.ntrUser.get().strip()
        psw = self.ntrPsw.get().strip()
        somma = self.ntrCifraPrelievo.get().strip()
        if self.bancomat.preleva(user, psw, somma):
            messagebox.showinfo("Operazione riuscita", "Denaro prelevato con successo!")
        else:
            messagebox.showwarning("Attenzione", "Operazione di prelievo non riuscita!")
        
    
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