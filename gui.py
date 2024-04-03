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
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox

"""class finestra_bancomat:
    def __init__(self, root):
        self.root = root
        #Non vanno
        self.root.title = "Bancomata MolPol"
        self.geometry = ("800x600")

    ## creazione dei bottoni
        
        #CLIENTE
        self.btn_prelievo = tk.Button(bg="yellow", text="Prelievo", width=25, height=3)
        self.btn_trasferisci = tk.Button(bg="pink", text="Trasferisci", width=25, height=3)
        self.btn_saldo = tk.Button(bg="light green", text="Saldo", width=25, height=3)

        #GESTORE:
        self.btn_prelievo = tk.Button(bg="yellow", text="Prelievo", width=25, height=3)
        self.btn_trasferisci = tk.Button(bg="pink", text="Trasferisci", width=25, height=3)
        self.btn_saldo = tk.Button(bg="light green", text="Saldo", width=25, height=3)
     


# attivazione dell'interfaccia
root = tk.Tk()
finestra_bancomat(root)
# task 4: avvio del ciclo ascolto eventi
root.mainloop()"""


bancomat = Bancomat()
bancomat.carica_da_file("bancomat.txt")
print(bancomat)

class myApp:
    def __init__ (self,root):
        self.root=root
        self.bancomat = Bancomat()
        
        #Aspetto
        self.root.title("Libri")
        #label con libri
        self.frame = tk.Frame(self.root,relief=tk.RAISED, borderwidth=1)
        self.frame.pack(fill=tk.BOTH,expand=True)
        self.librivar = tk.StringVar()
        self.libri = tk.Label(self.frame, textvariable=self.librivar)
        self.libri.pack(fill=tk.BOTH,expand=True)

        #bottoni
        self.btn_1=tk.Button(text="Carica da file",background="light green",width=20)
        self.btn_2=tk.Button(text="Salva su file",background="light blue",width=20)
        self.btn_3=tk.Button(text="Inserisci Libro",background="orange",width=20)
        self.btn_4=tk.Button(text="Elimina Libro",background="yellow",width=20)

        self.btn_1.pack(side = tk.LEFT)
        self.btn_2.pack(side = tk.LEFT)
        self.btn_3.pack(side = tk.LEFT)
        self.btn_4.pack(side = tk.LEFT)

        #bind
        self.btn_1.bind("<Button-1>", self.carica)
        self.btn_2.bind("<Button-1>", self.salva)
        self.btn_3.bind("<Button-1>", self.inserisci)
        self.btn_4.bind("<Button-1>", self.elimina)

        #entry
        self.entry = tk.Entry(self.root, width=100)
        self.entry.pack(side = tk.LEFT, expand=True)

    def carica(self, evento):
        self.catologo.read_from_file(self.entry.get())
        self.librivar.set(self.catologo)
    def salva(self, evento):
        self.catologo.write_to_file(self.entry.get())
    def inserisci(self, evento):
        libro = self.entry.get().split(":")
        self.catologo.aggiungi_libro(Libro(libro[0],libro[1],libro[2],libro[3]))
        self.librivar.set(self.catologo)
    def elimina(self, evento):
        self.catologo.elimina_libro(int(self.entry.get()))
        self.librivar.set(self.catologo)

w = tk.Tk()
myApp(w)
w.mainloop()