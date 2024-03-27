# Creare tre Classi: Utente, Cliente e Admin. Cliente e Admin sono sottoclassi di Utente.
# Tutti i metodi che modificano lo stato devono lanciare opportune eccezioni ValueError o TypeError se i parametri non sono corretti.

# La classe Utente ha un costruttore che prende in input lo username (stringa).
# Ha i metodi set_username, get_username, il metodo di confronto di uguaglianza e il metodo __repr__.

# La classe Cliente ha un costruttore che prende in input lo username (stringa), il pin (stringa composta da 6 cifre), il nome (stringa) e il cognome (stringa).
# Ha i metodi getter e setter per lo stato, il metodo __str_ e il metodo di confronto di uguaglianza.
# Rappresentazione stringa: "Cliente: username pin nome cognome" e.g. "Cliente: mario.rossi 123456 Mario Rossi"

# La classe Admin ha un costruttore che prende in input lo username (stringa) e la password (stringa con almeno una cifra e una lettera).
# Ha i metodi getter e setter per lo stato, il metodo __str__ e il metodo di confronto di uguaglianza.
# Rappresentazione stringa: "Admin: username password" e.g. "Admin: mario Password123"

# Inserire il codice qui sotto


import re

#Classe Utente
class Utente:
    def __init__(self, initUser):
        if not isinstance(initUser, str):
            raise TypeError("Lo username deve essere una stringa")
        self.username = initUser

    def get_username(self):
        return self.username

    def set_username(self, newUser):
        if not isinstance(newUser, str):
            raise TypeError("Lo username deve essere una stringa")
        self.username = newUser

    def __repr__(self):
        return "Utente = " + str(self.username)

    def __eq__(self, otherUtente):
        if isinstance(otherUtente, Utente):
            return self.username == otherUtente.username
        return False

#Classe Cliente
class Cliente(Utente):
    def __init__(self, initUser, initPin, initNome, initCognome):
        #Eredita username dalla superclasse Utente
        super().__init__(initUser)

        #Controlli su pin (stringa di 6 cifre)
        if not isinstance(initPin, str) or not initPin.isalpha(): 
            raise TypeError("Il pin deve essere una stringa di numeri")
        else:
            if not re.match(r'^\d{6}$', initPin):
                raise ValueError("Il pin deve essere composto da 6 cifre")
        self.pin = initPin

        #Controlli su nome (stringa di char)
        if not isinstance(initNome, str) or not initNome.isalpha():
            raise TypeError("Il nome deve essere una stringa di caratteri")
        self.nome = initNome

        #Controlli su cognome (stringa di char)
        if not isinstance(initCognome, str) or not initCognome.isalpha():
            raise TypeError("Il cognome deve essere una stringa di caratteri")
        self.cognome = initCognome

    #Getter e setter per pin
    def get_pin(self):
        return self.pin
    
    def set_pin(self, newPin):
        if not isinstance(newPin, str) or not newPin.isalpha():
            raise TypeError("Il pin deve essere una stringa di numeri") 
        else:
            if not re.match(r'^\d{6}$', newPin):
                raise ValueError("Il pin deve essere composto da 6 cifre")
        self.pin = newPin

    #Getter e setter per nome
    def get_nome(self):
        return self.nome

    def set_nome(self, newNome):
        if not isinstance(newNome, str) or not newNome.isalpha():
            raise TypeError("Il nome deve essere una stringa di caratteri")
        self.nome = newNome
    
    #Getter e setter per cognome
    def get_cognome(self):
        return self.cognome
    
    def set_cognome(self, newCognome):
        if not isinstance(newCognome, str) or not newCognome.isalpha():
            raise TypeError("Il cognome deve essere una stringa di caratteri")
        self.cognome = newCognome

    #Metodo di stampa dell'oggetto secondo le modalità indicate
    def __str__(self):
        return "Cliente: " + str(self.username) + " " + str(self.pin) + " " + str(self.nome) + " " + str(self.cognome)
    
    #Metodo di controllo dell'uguaglianza per due istanze dello stesso oggetto
    def __eq__(self, otherCliente):
        if isinstance(otherCliente, Cliente):
            # Confronto degli attributi specifici della classe Cliente e quelli ereditati dalla classe Utente
            if (self.username == otherCliente.username and
                self.pin == otherCliente.pin and
                self.nome == otherCliente.nome and
                self.cognome == otherCliente.cognome):
                return True
        return False


#Classe Admin
class Admin(Utente):
    #Metodo costruttore
    def __init__(self, initUser, initPassword):
        #Admin eredita username dalla superclasse Utente
        super().__init__(initUser)

        #Controlli per la password (stringa composta da almeno una lettera e almeno un numero)
        #Controllo effettuato con regex
        if not isinstance(initPassword, str) and not re.match(r'^(?=.[A-Za-z])(?=.\d).+$', initPassword):
            raise ValueError("La password deve contenere almeno un carattere e almeno una cifra")
        self.password = initPassword

    #Metodi getter e setter per password
    def get_password(self):
        return self.password
    
    def set_password(self, newPassword):
        #Controllo su password
        if not isinstance(newPassword, str) or not re.match(r'^(?=.[A-Za-z])(?=.\d).+$', newPassword):
            raise ValueError("La password deve contenere almeno un carattere e almeno una cifra")
        self.password = newPassword

    #Metodo di stampa per l'oggetto Admin secondo le modalità indicate
    def __str__(self):
        return "Admin: " + str(self.username) + " " + str(self.password)
    
    #Metodo di controllo dell'uguaglianza tra due istanze della stessa classe
    def __eq__(self, otherAdmin): 
        if isinstance(otherAdmin, Admin):
            if (self.username == otherAdmin.username and
                self.password == otherAdmin.password):
                return True
        return False