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
from tkinter import Tk
from tkinter import messagebox

class BancomatApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Bancomat Molpol")
        #self.root.geometry("300x300")
        #Utilizzo di grid per posizionare il frame principale
        self.frame = tk.Frame(self.root, relief=tk.RAISED, borderwidth=1)
        self.frame.grid(row=0, column=0, sticky="nsew")

        btnCarica = tk.Button(
            text="Carica File", 
            width=20,
            height=5,
            bg="grey",
            fg="black",
            #command=self.read_from_file(),
        )

        #Label, Entry e rispettivi grid
        #Archivio da cercare per caricarlo o salvarlo 
        self.cerca = tk.Label(self.frame, text="Nome archivio:")
        self.cerca.grid(row=2, column=0, padx=2, pady=2, sticky="w")
        #Campo di ricerca dell'archivio
        self.entry_cerca_arc = tk.Entry(self.frame, width=30)
        self.entry_cerca_arc.grid(row=2, column=1, padx=2, pady=2)
        #Bottoni associati al campo dove inserire il nome dell'archivio
        self.btnCarica = tk.Button(self.frame, text="Carica archivio")
        self.btnCarica.grid(row=2, column=2, padx=2, pady=2)
        self.btn_salva = tk.Button(self.frame, text="Salva archivio")
        self.btn_salva.grid(row=3, column=1, padx=2, pady=2)



        #self.btnCarica.pack()
        userAdmin, pswAdmin = self.read_from_file("bancomat.txt")
        systemAdmin = Admin(userAdmin, pswAdmin)
        bancomat = Bancomat(systemAdmin, 0, 0)
        bancomat.carica_da_file(userAdmin, pswAdmin, "bancomat.txt")
        print(bancomat)


        #Lista dei bind()
        self.btnCarica.bind("<Button-1>", self.btn_archivio_premuto)
        

    #def handle_btnCarica_press(event):
    def btn_archivio_premuto(self, event):
        #Quando il bottone è stato premuto:
        #imposto la variabile a True 
        self.premuto_var.set(True)
        #associo l'evento che carica l'archivio
        self.carica_archivio(event)
    
    def carica_archivio(self, evento):
        #Prendo il nome dell'archivio dalla casella di testo associata
        nome_archivio = self.entry_cerca_arc.get()
        #Verifico che il nome dell'archivio sia stato inserito e che sia stato cliccato il bottone per caricare l'archivio
        if not(nome_archivio and self.premuto_var.get()):
            #Mostro un messaggio di avvertimento se il nome dell'archivio non è stato inserito nel campo corrispondente
            messagebox.showwarning("Attenzione", "Caricare il file con l'archivio prima di fare qualunque azione.")
            return
        else:
            #Altrimenti l'archivio viene caricato in base a entry_cerca_arc.get()
            self.archivio.carica(nome_archivio)
            #In seguito viene aggiornata la visualizzazione dell'interfaccia con l'intero archivio caricato
            self.studvar.set(self.archivio)
         
    #FUNZIONE CHE LEGGE LE CREDENZIALI DELL'ADMIN DI SISTEMA
    def read_from_file(self, filename):
        try:
            #carico il file in lettura 
            with open(filename, "r") as file:
                for riga in file:
                    riga = riga.strip()
                    if riga.startswith("Admin:"):
                        user, psw = riga.split()[1:3]
                        return user, psw
        except IOError:
                #print("Errore nell'apertura del file: " + filename)
                return False 

window = tk.Tk()
BancomatApp(window)
window.mainloop()