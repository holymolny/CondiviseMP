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

class BancomatApp():
    def __init__(self):
        self.title("Bancomat Molpol")
        self.geometry("300x300")

        bancomat = Bancomat({},0,0)
        bancomat.carica_da_file()
        print(bancomat)

    #FUNZIONE CHE MI SERVE PER CARICARE IL FILE DATI
    def carica_file(self):
        try:
            #carico il file in lettura 
            with open("bancomat.txt", "r") as file:
                stato_bancomat = file.read()
                self.bancomat.carica_stato(stato_bancomat)
        except FileNotFoundError:
            messagebox.showerror("Errore", "Non è stato trovato il file bancomat.txt")
            self.destroy()




app = BancomatApp
app.mainloop()