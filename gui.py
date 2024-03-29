from bancomat import *
from utenti import *
import tkinter as tk
from tkinter import Tk

class BancomatGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bancomat")
        self.current_user = None

        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack()
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()

        self.operation_frame = tk.Frame(self.master)
        self.error_label = tk.Label(self.master, fg="red")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            user = self.bancomat.login(username, password)
            self.current_user = user
            self.show_operations()
        except BancomatError as e:
            self.show_error(str(e))

    def show_operations(self):
        self.login_frame.pack_forget()
        self.error_label.pack_forget()

        if isinstance(self.current_user, Cliente):
            self.show_client_operations()
        elif isinstance(self.current_user, Admin):
            self.show_admin_operations()
        else:
            self.show_error("Tipo di utente non riconosciuto.")

    def show_client_operations(self):
        self.operation_frame.pack()
        self.withdraw_button = tk.Button(self.operation_frame, text="Prelievo", command=self.withdraw)
        self.withdraw_button.pack()
        self.deposit_button = tk.Button(self.operation_frame, text="Deposito", command=self.deposit)
        self.deposit_button.pack()
        self.transfer_button = tk.Button(self.operation_frame, text="Trasferimento", command=self.transfer)
        self.transfer_button.pack()

    def show_admin_operations(self):
        self.operation_frame.pack()
        self.manage_users_button = tk.Button(self.operation_frame, text="Gestione Utenti", command=self.manage_users)
        self.manage_users_button.pack()

    def withdraw(self):
        # Implementa la logica per il prelievo
        pass

    def deposit(self):
        # Implementa la logica per il deposito
        pass

    def transfer(self):
        # Implementa la logica per il trasferimento
        pass

    def manage_users(self):
        # Implementa la gestione degli utenti (solo per admin)
        pass

    def show_error(self, message):
        self.error_label.config(text=message)
        self.error_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BancomatGUI(root)
    root.mainloop()