from bancomat import *
import tkinter as tk
from tkinter import *
from tkinter import ttk

def login():
    print('ho cliccato sul bottone LogIn')

#CREO FINESTRA

#finestra principale:
root = Tk()
root.title('Bancomat MOLPOL')
#dimensione della finestra:
root.geometry('800x600')
root.resizable(False, False)
#per farla comparire davanti alle altre schede
root.lift()

#testo centrale
label = Label(text = 'MOLPOL BANKING SYSTEM', font = ('Calibri', 20))
label.pack()

#bottone login
button = Button(text = "LogIn", command=login)
button.pack()
#bottone meme che chiude il programma
button = Button(text = "Stacca Stacca", command = lambda: root.quit())
button.pack()

root.mainloop()