from bancomat import *
import tkinter as tk

# Funzione chiamata quando il pulsante viene premuto
def button_click():
    label.config(text="Hai premuto il pulsante!")

# Creazione di una nuova finestra
window = tk.Tk()

# Aggiunta di un titolo alla finestra
window.title("Esempio Tkinter")

# Creazione di un'etichetta nella finestra
label = tk.Label(window, text="Ciao, Tkinter!")
label.pack()  # Posiziona l'etichetta nella finestra

# Creazione di un pulsante nella finestra
button = tk.Button(window, text="Premimi!", command=button_click)
button.pack()  # Posiziona il pulsante nella finestra

# Avvio del ciclo di eventi della finestra
window.mainloop()