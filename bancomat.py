from utenti import *
# Da completare con il codice

USER = ""
PSW = ""
ADMIN = False

#CLASSE Bancomat
class Bancomat:
    LOGIN_ERRATO = "Login errato"
    FONDI_INSUFFICIENTI = "Fondi insufficienti"
    LIMITE_PRELIEVO_SUPERATO = "Limite prelievo superato"
    UTENTE_NON_VALIDO = "Utente non valido"    

    """
    -STATO:
        utenti: dizionario che ha come chiave username e come valore una coppia con il riferimento ad un utente e il suo saldo.
        scoperto_massimo: intero >= 0 che rappresenta il massimo scoperto che un cliente può avere sul proprio conto.
        limite_prelievo: intero >= 0 che rappresenta il massimo prelievo che un cliente può fare in una volta sola.
    
    Gli utenti di tipo Admin devono avere sempre saldo 0

    -COSTRUTTORE da inserire come primo metodo della classe Bancomat:
        Prende come argomenti un Admin, un intero positivo rappresentante lo scoperto massimo e un intero positivo rappresentante il limite di prelievo.
        Controlla tipi e valori degli argomenti e solleva un'eccezione TypeError o ValueError se non sono corretti.
        Inizializza l'oggetto Bancomat inserendo l'admin nel dizionario utenti.

    """
    def __init__(self, initAdmin, initScoperto, initPrelievo):
        #initAdmin deve essere oggetto classe Admin
        if not isinstance(initAdmin, Admin):
            raise TypeError("L'utente inserito non è admin del sistema")
        self.admin = initAdmin

        #initScoperto deve essere >0
        if not isinstance(initScoperto, int):
            raise TypeError("Lo scoperto deve essere un numero intero")
        else: 
            if (initScoperto < 0):
                raise ValueError("Lo scoperto non può assumere valore negativo")
            self.scoperto_massimo = initScoperto

        #initPrelievo deve essere >0
        if not isinstance(initPrelievo, int):
            raise TypeError("Il limite massimo per il prelievo deve essere un numero intero")
        else:
            if (initPrelievo < 0):
                raise ValueError("Il limite per il prelievo non può assumere valore negativo")
            self.limite_prelievo = initPrelievo
        
        #Viene creato il dizionario degli utenti
        self.utenti = {self.admin.get_username(): (self.admin,  0)}
        
        

    """"
    -METODO DI RAPPRESENTAZIONE STRINGA:
       Restituisce una stringa che rappresenta l'oggetto Bancomat nel formato:
        "Bancomat: scoperto massimo, limite prelievo
        lista utenti uno per riga con saldo per i clienti"
        Esempio:
        "Bancomat: 1000, 500
        Admin: username1 password2
        Cliente: username2 111111 nome cognome 0
        Cliente: username3 000000 nome cognome 0
        "
        Se la lista utenti è vuota la seconda riga deve esssere "Nessun utente presente".
    """
    
    #Funzione che stampa la stringa
    def __str__(self):
        strBancomat =  "Bancomat: " + str(self.scoperto_massimo) + ", " + str(self.limite_prelievo)
        for (utente, valore) in self.utenti.items():
            strBancomat += '\n Utente: ' + str(utente) + ", " + str(valore)
        return strBancomat
    
    """"
    -METODO DI CONFRONTO DI UGUAGLIANZA:
        Confronta due Bancomat e restituisce true se scoperto_massimo e limite_prelievo sono uguali e se la lista utenti contiene gli stessi utenti.
    """

    def __eq__(self, other):
        if not isinstance(other, Bancomat):
            return False
        
        if self.scoperto_massimo != other.scoperto_massimo or self.limite_prelievo != other.limite_prelievo:
            return False
        
        if sorted(self.utenti.keys()) != sorted(other.utenti.keys()):
            return False
        
        for username, (utente_self, saldo_self) in self.utenti.items():
            if username not in other.utenti:
                return False
            utente_other, saldo_other = other.utenti[username]
            if type(utente_self) != type(utente_other) or saldo_self != saldo_other:
                return False
        
        return True   

    """"
    -METODI GETTER classici per lo stato senza login (GETTER e SETTER con login sono specificati sotto))
    """

    def get_admin(self):
        return self.admin
    
    def get_limite_prelievo(self):
        return self.limite_prelievo
    
    def get_scoperto_massimo(self):
        return self.scoperto_massimo
    
    def get_utenti(self):
        return self.utenti
    

    def login(self, username, secret, isAdmin=False):
        """Controlla che un utente sia presente nel dizionario, che il secret (pin o password) sia corretto e se isAdmin è True che l'utente sia un Admin.
        :param username: lo username dell'utente
        :param secret: la password o il pin dell'utente
        :param isAdmin: booleano che indica se l'operazione è per un Admin
        :return: True se il login è riuscito, False altrimenti
        """
        global USER
        global PSW
        global ADMIN
        
        logIn = False
        if username in self.utenti:
            utente = self.utenti[username][0]
            if isAdmin and isinstance(utente, Admin):
                if utente.get_password() == secret:
                    logIn = True
                    USER = utente.get_username()
                    PSW = utente.get_password()
                    ADMIN = True
            elif not isAdmin and isinstance(utente, Cliente):
                if utente.get_pin() == secret:
                    logIn = True
                    USER = utente.get_username()
                    PSW = utente.get_pin()
                    ADMIN = False
            
            return logIn


    def get_limite_prelievo(self, username, secret):
        """Restituisce il limite massimo di prelievo dopo aver effettuato il login.
        :param username: lo username dell'utente
        :param secret: la password o il pin dell'utente
        :return: il limite massimo di prelievo, None se il login non è riuscito
        """
        #pass #istruzione che non fa niente --> da sostituire con il codice
        if(USER == username and PSW == secret):
            return self.limite_prelievo
        

    def set_limite_prelievo(self, username, password, limite_prelievo):
        """Modifica il limite massimo di prelievo dopo aver effettuato il login.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :param limite_prelievo: il nuovo limite massimo di prelievo
        :return: True se il limite massimo di prelievo è stato modificato, False altrimenti
        """
        #pass #istruzione che non fa niente --> da sostituire con il codice
        if(username == USER and password == PSW and ADMIN): #Verifico di essere loggato al sistema
            self.limite_prelievo = limite_prelievo
            return True
    
    def get_scoperto_massimo(self, username, secret):
        """Restituisce lo scoperto massimo ammesso nel bancomat dopo aver effettuato il login.
        :param username: lo username dell'utente
        :param secret: la password o il pin dell'utente
        :return: lo scoperto massimo ammesso, None se il login non è riuscito
        """
        #pass #istruzione che non fa niente --> da sostituire con il codice
        if(username == USER and secret == PSW):
            return self.scoperto_massimo
       

    def set_scoperto_massimo(self, username, password, scoperto_massimo):
        """Modifica lo scoperto massimo ammesso nel bancomat dopo aver effettuato il login.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :param scoperto_massimo: il nuovo scoperto massimo
        :return: True se lo scoperto massimo è stato modificato, False altrimenti        
        """
        #pass #istruzione che non fa niente --> da sostituire con il codice
        if(USER == username and PSW == password and ADMIN):
            if isinstance(scoperto_massimo, int):
                if(scoperto_massimo > 0):
                    self.scoperto_massimo = scoperto_massimo
                    return True
        return False

    def get_saldo(self, username, pin):
        """Restituisce il saldo del Cliente dopo aver effettuato il login.
        :param username: lo username del cliente che vuole sapere il saldo
        :param pin: il pin del cliente
        :return: il saldo del cliente, None se il login non è riuscito
        """
        #pass #istruzione che non fa niente --> da sostituire con il codice
        if (USER == username and PSW == pin and not ADMIN):
            saldo = self.utenti[username][1]
            return saldo
    
    def get_lista_utenti(self, username, password):
        """Restituisce la lista degli utenti ad un Admin dopo aver effettuato il login.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :return: lista degli utenti, None se il login non è riuscito
        """
        if (USER == username and PSW == password and ADMIN):
            lista_utenti = []
            for key in self.utenti.keys():
                lista_utenti.append(self.utenti[key][0])
            return lista_utenti
        
            
    
    def get_utente(self, username, password, u_utente):
        """Restituisce l'oggento Utente cercato ad un Admin dopo aver effettuato il login.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :param u_tente: l'username dell'utente da cercare
        :return: l'utente cercato, None se il login non è riuscito o l'utente non esiste
        """
        #pass #istruzione che non fa niente --> da sostituire con il codice
        if USER == username and PSW == password and ADMIN:
            if u_utente in self.utenti.keys():
                return self.utenti[u_utente][0]
    
    def aggiungi_utente(self, username, password, utente, somma=0):
        """Aggiunge un utente non presente al sistema dopo aver effettuato il login.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :param utente: oggetto di tipo utente da aggiungere
        :param somma: la somma iniziale dell'utente
        :return: True se l'utente è stato aggiunto, False altrimenti
        """
        isAdded = False
        if username == USER and password == PSW:
            if not utente.get_username() in self.utenti:
                if isinstance(utente, Admin):
                    if somma == 0:
                        self.utenti[utente.get_username()] = (utente, somma)
                        isAdded = True
                    #altrimenti genera eccezione
                    else:
                        raise ValueError("Saldo non valido per Admin")
                else:
                    self.utenti[utente.get_username()] = (utente, somma)
                    isAdded = True
        return isAdded

    def rimuovi_utente(self, username, password, u_utente):
        """Rimuove un utente dal sistema dopo aver effettuato il login.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :param u_utente: l'username dell'utente da rimuovere
        :return: True se l'utente è stato rimosso, False altrimenti
        """
        #pass #istruzione che non fa niente --> da sostituire con il codice
        if (USER == username and PSW == password and ADMIN):
            if u_utente in self.utenti.keys():
                del self.utenti[u_utente]
                return True
        return False

    def modifica_somma(self, username, password, u_utente, somma):
        """Modifica la somma di un utente del sistema dopo aver effettuato il login.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :param u_utente: l'username dell'utente di cui modificare la somma
        :param somma: la nuova somma
        :return: True se la somma è stata modificata, False altrimenti
        """
        if (USER == username and PSW == password and ADMIN):
            if u_utente in self.utenti.keys():
                somma = self.utenti[u_utente][1]
                return True
        return False

    def modifica_pin(self, username, secret, new_secret):
        """Modifica il pin di un utente dopo aver effettuato il login.
        :param username: lo username dell'utente
        :param secret: il vecchio secret dell'utente (pin o password)
        :param new_secret: il nuovo secret dell'utente (pin o password)
        :return: True se il pin è stato modificato, False altrimenti
        """
        #pass #istruzione che non fa niente --> da sostituire con il codice
        if USER == username and PSW == secret:
            utente = self.utenti[username][0]
            if isinstance(utente, Admin):
                


                
    def preleva(self, username, pin, somma):
        """Permette ad un cliente di prelevare dal proprio conto dopo aver effettuato il login, prelevando al massimo "limite_prelievo" e andando in negativo di al massimo "scoperto_massimo".
        :param username: lo username del cliente
        :param pin: il pin del cliente
        :param somma: la somma da prelevare
        :return: coppia (True, "") se il prelievo è riuscito, (False, motivazione) altrimenti. La motivazione deve essere una delle stringhe dichiarate sotto la definizione della classe.
        """
        pass #istruzione che non fa niente --> da sostituire con il codice

    def deposita(self, username, pin, somma):
        """Permette ad un cliente di depositare sul proprio conto dopo aver effettuato il login.
        :param username: lo username del cliente
        :param pin: il pin del cliente
        :param somma: la somma da depositare
        :return: coppia (True, "") se il deposito è riuscito, (False, motivazione) altrimenti. La motivazione deve essere una delle stringhe dichiarate sotto la definizione della classe.
        """
        pass #istruzione che non fa niente --> da sostituire con il codice

    def trasferisci(self, username, pin, destinatario, somma):
        """Permette ad un cliente di trasferire ad un altro cliente dopo aver effettuato il login, andando in negativo di al massimo "scoperto_massimo".
        :param username: lo username del cliente
        :param pin: il pin del cliente
        :param destinatario: username del cliente destinatario del trasferimento
        :param somma: la somma da trasferire
        :return: coppia (True, "") se il trasferimento è riuscito, (False, motivazione) altrimenti. La motivazione deve essere una delle stringhe dichiarate sotto la definizione della classe.
        """
        pass #istruzione che non fa niente --> da sostituire con il codice
      
    def lista_clienti_con_saldo_negativo(self, username, password):
        """Restituisce la lista dei clienti con saldo negativo dopo aver effettuato il login.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :return: lista di oggetti clienti con saldo negativo, None se il login non è riuscito
        """
        pass #istruzione che non fa niente --> da sostituire con il codice
        
    def lista_clienti_con_saldo_almeno(self, username, password, somma=0):
        """Restituisce la lista dei clienti con saldo almeno "somma" dopo aver effettuato il login.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :param somma: la somma minima
        :return: lista di oggetti clienti con saldo almeno "somma", None se il login non è riuscito
        """
        pass #istruzione che non fa niente --> da sostituire con il codice

    def salva_su_file(self, username, password, filename):
        """Salva scoperto_massimo, limite_prelievo e gli utenti su un file dopo aver effettuato il login (gestire eccezioni relative ai file).
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :param filename: il nome del file su cui salvare gli utenti
        :return: True se il salvataggio è riuscito, False altrimenti
        """
        pass #istruzione che non fa niente --> da sostituire con il codice
    
    def carica_da_file(self, username, password, filename):
        """Carica scoperto_massimo, limite_prelievo e gli utenti da un file dopo aver effettuato il login (gestire eccezioni relative ai file).
        Sovrascrive lo stato attuale del Bancomat.
        :param username: lo username dell'admin
        :param password: la password dell'admin
        :param filename: il nome del file da cui caricare gli utenti
        :return: True se il caricamento è riuscito, False altrimenti
        """
        pass #istruzione che non fa niente --> da sostituire con il codice
    
