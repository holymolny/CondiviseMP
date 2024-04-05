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
        self.root.geometry("500x420")
        window.resizable(False,False)
    
    # Creazione dei frame che suddividono la window
        self.frame1 = tk.Frame(master = window, background="light blue", width=500, height=20)
        self.frame2 = tk.Frame(master = window)
        self.frame3 = tk.Frame(master = window, background="light blue", width=500, height=20)
        self.frame4 = tk.Frame(master = window)
    # Posizionamento dei frame all'interno della finestra principale
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
    
        #TITOLO
        self.titolo = tk.Label(
            self.frame2,
            text ="Bancomat MolPol",
            background="light blue",
            width = 500,
            foreground="white",
            font=('Helvetica', 20),
            anchor= "center"
            )
        self.titolo.pack()

        self.btnLoad = tk.Button(self.frame4, text="Carica Dataset", background="light blue", width=20, anchor="center")
        self.btnLoad.pack()
        
window = tk.Tk()
BancomatApp(window)
window.mainloop()