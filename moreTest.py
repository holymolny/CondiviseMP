from bancomat import *
from testMy import *

#Registra se ci sono errori
errori = 0

mainAdmin = Admin("admin1", "admin123")
secondAdmin = Admin("admin2", "admin123")
bancomat = Bancomat(mainAdmin, 500, 1000)

#print(mainAdmin, secondAdmin, bancomat)


#Test creazione utenti
cliente1 = Cliente("cl1", "123456", "Mario", "Rossi")
cliente2 = Cliente("cl2", "000000", "Lucia", "Bianchi")
cliente3 = Cliente("cl3", "111111", "Giovanni", "Verdi")
cliente4 = Cliente("cl4", "222222", "Anna", "Neri")


try:
    Cliente("clx", 123456, "Mario", "Rossi")
    errori += 1
    print(f"Test {4}: Failed")
except TypeError:
    pass


try:
    Cliente("clx", "123456", 123456, "Rossi")
    errori += 1
    print(f"Test {5}: Failed")
except TypeError:
    pass

try:
    Cliente("clx", "aaaaa", "Mario", "Rossi")    
    errori += 1
    print(f"Test {6}: Failed")
except ValueError:
    pass

try:
    Cliente("clx", "12345a", "Mario", "Rossi")
    errori += 1
    print(f"Test {7}: Failed")
except ValueError:
    pass

try:
    Cliente("clx", "12345", "Mario", "Rossi")
    errori += 1
    print(f"Test {8}: Failed")
except ValueError:
    pass

try:
    adminx = Admin("adminx", "adminx")
    errori += 1
    print(f"Test {9}: Failed")

except ValueError:
    pass

try:
    adminx = Admin("adminx", "12345678")
    errori += 1
    print(f"Test {10}: Failed")
except ValueError:
    pass

####################################Da chiedere al professore
#Non genera eccezione ma non la deve generare perchè i dati in input sono corretti
"""try:
    adminx = Admin("adminx", "a1")
    errori += 1
    print(f"Test {11}: Failed")
except ValueError:
    pass"""


#LOGIN DI ADMIN
bancomat.login("admin1", "admin123", True)

#AGGIUNTA ELEMENTI AL DIZIONARIO
errori += testEqual(12, bancomat.aggiungi_utente("admin1", "admin123",cliente1,1000), True)
errori += testEqual(13, bancomat.aggiungi_utente("admin1", "admin123",cliente1,1000), False)
errori += testEqual(14, bancomat.aggiungi_utente("admin1", "admin123",cliente2), True)
errori += testEqual(15, bancomat.aggiungi_utente("admin1", "admin123",cliente3,500), True)
errori += testEqual(16, bancomat.aggiungi_utente("admin1", "admin123",cliente4,1500), True)

try:
    errori += testEqual(17, bancomat.aggiungi_utente("admin1", "admin123",secondAdmin,1000), False)
    print(f"Test {17}: Failed")
except ValueError:
    pass

errori += testEqual(18, bancomat.aggiungi_utente("admin1", "admin123",secondAdmin,0), True)

#Test su get_lista_utenti()
errori += testEqual(19, bancomat.get_lista_utenti("admin1", "admin123"), [mainAdmin, cliente1, cliente2, cliente3, cliente4, secondAdmin])


#PROVE LOGIN 

#Test login admin
errori += testEqual(20, bancomat.login("admin1", "admin123",True), True)
errori += testEqual(21, bancomat.login("admin1", "admin2",True), False)

#############################################CHIEDERE AL PROF#####################################################
"""errori += testEqual(22, bancomat.login("admin1", "admin123",False), True)"""
#Secondo me stampa il valore corretto che è questo
#print(bancomat.login("admin1", "admin123",False))
##################################################################################################################


#Test login clienti
try: #genera eccezione perchè la psw deve contenere almeno un char
    errori += testEqual(23, bancomat.modifica_pin("admin1", "admin123", "123456"), False) 
    print(f"Test {4}: Failed")
except ValueError:
    pass

errori += testEqual(24, bancomat.login("cl2", "000000",False), True)
errori += testEqual(25, bancomat.login("cl2", "000001",False), False)
errori += testEqual(26, bancomat.login("cl2", "000000",True), False)
errori += testEqual(27, bancomat.modifica_pin("cl2", "000000", "123456"), True)

#Test login clienti post modifica_pin()
errori += testEqual(28, bancomat.login("cl2", "123456",False), True)
errori += testEqual(29, bancomat.login("cl2", "000001",False), False)
errori += testEqual(30, bancomat.login("cl2", "123456",True), False)

####################################### TEST DI MAIN.PY ##########################################################
"""print(bancomat.login("cl2", "123456"))
print(bancomat.preleva("cl2", "123456", 100))"""
errori += testEqual(31, bancomat.preleva("cl2", "123456", 100), (True,"")) #-100
errori += testEqual(32, bancomat.preleva("cl2", "123456", 2000), (False, Bancomat.LIMITE_PRELIEVO_SUPERATO))
errori += testEqual(33, bancomat.preleva("cl2", "123456", 500), (False, Bancomat.FONDI_INSUFFICIENTI))
errori += testEqual(34, bancomat.preleva("cl2", "123455", 100), (False, Bancomat.LOGIN_ERRATO))
errori += testEqual(35, bancomat.deposita("cl2", "123456", 1000), (True,"")) #90
"""print(bancomat.deposita("cl2", "123456", 1000))
print(bancomat.utenti["cl2"][1])"""

errori += testEqual(36, bancomat.preleva("cl2", "123456", 500), (True, "")) #400
errori += testEqual(37, bancomat.trasferisci("cl2", "123456", "cl3", 500), (True,"")) #-100
errori += testEqual(38, bancomat.trasferisci("cl2", "123456", "admin1", 1), (False, Bancomat.UTENTE_NON_VALIDO))
errori += testEqual(39, bancomat.trasferisci("cl2", "123456", "cl3", 500), (False, Bancomat.FONDI_INSUFFICIENTI))
errori += testEqual(40, bancomat.get_saldo("cl2", "123456"), -100)
errori += testEqual(41, bancomat.deposita("admin1", "admin123", 1000), (False, Bancomat.UTENTE_NON_VALIDO)) #admin non può cambiare il saldo
errori += testEqual(42, bancomat.preleva("admin1", "admin123", 100), (False, Bancomat.UTENTE_NON_VALIDO)) #admin non può cambiare il saldo"""


"""print(bancomat.modifica_pin("cl2", "000000", "123456"))"""
#print(bancomat.login("cl2", "123456",False))
#Test preleva()
"""print(bancomat.preleva("cl2", "123456", 100))
print(bancomat.preleva("cl2", "123456", 2000))
print(bancomat.preleva("cl2", "123456", 500))
print(bancomat.preleva("cl2", "123455", 100))
errori += testEqual(43, bancomat.preleva("cl2", "123456", 100), (True,"")) #-100
errori += testEqual(44, bancomat.preleva("cl2", "123456", 2000), (False, Bancomat.LIMITE_PRELIEVO_SUPERATO))
errori += testEqual(45, bancomat.preleva("cl2", "123456", 500), (False, Bancomat.FONDI_INSUFFICIENTI))
errori += testEqual(46, bancomat.preleva("cl2", "123455", 100), (False, Bancomat.LOGIN_ERRATO))"""

#TEST GET_LIMITE_PRELIEVO
errori += testEqual(47, bancomat.get_limite_prelievo("cl1", "123456"), None)   #1000 quando è loggato
errori += testEqual(48, bancomat.get_limite_prelievo("admin1", "admin123"), 1000)
errori += testEqual(49, bancomat.get_limite_prelievo("cl7", "123456"), None)  #Non esiste qundi ritorna None

#DEBUG DI GET_LIMITE_PRELIEVO
"""
Per prendere il limite di prelievo con la funzione sotto, 
devo prima essermi loggato al sistema, altrimenti da errore (restituisce None)
"""
"""
bancomat.login("cl1", "123456", False)
print(bancomat.get_limite_prelievo("cl1", "123456")) #1000
bancomat.login("admin1", "admin123", True)
print(bancomat.get_limite_prelievo("admin1", "admin123")) #1000
print(bancomat.get_limite_prelievo("cl7", "123456")) #None
"""

#Test Set_limite_prelievo()
#print(bancomat.set_limite_prelievo("admin1", "admin123", 2000)) 
#print(bancomat.set_limite_prelievo("cl1", "123456", 3000)) #Errore perchè non è loggato


errori += testEqual(50, bancomat.set_limite_prelievo("cl1", "123456", 2000), None)   #None perchè non riesce a cambiare il limite dato che non è Admin
errori += testEqual(51, bancomat.get_limite_prelievo("admin1", "admin123"), 1000)



#Test get_scoperto_massimo():

errori += testEqual(52, bancomat.get_scoperto_massimo("admin1", "admin123"), 500)
bancomat.login("cl1", "123456")
errori += testEqual(53, bancomat.get_scoperto_massimo("cl1", "123456"), 500)  


#Test set_scoperto_massimo

bancomat.login("cl1", "123456", False)
errori += testEqual(54, bancomat.set_scoperto_massimo("cl1", "123456", 2000), False)  #False perchè il cliente non può effettuare l'operazione
bancomat.login("admin1", "admin123", True)
errori += testEqual(55, bancomat.set_scoperto_massimo("admin1", "admin123", 2000), True)

#Test funzione get_saldo()


#Test su rimuovi utente
errori += testEqual(56, bancomat.rimuovi_utente("admin1", "admin123","cl1"), True)
errori += testEqual(57, bancomat.rimuovi_utente("admin3", "admin123","cl1"), False) #False perchè admin3 non esiste
errori += testEqual(58, bancomat.rimuovi_utente("admin1", "admin123","cl7"), False)


#Test su modifica_somma
errori += testEqual(59, bancomat.modifica_somma("admin1", "admin123","cl3", 1000), True)

#Stampa se ci sono errori
# abbiamo finito ?
if errori == 0:
    print(bancomat)
    print("\t****Test completati -- effettuare la consegna come da README")
else:
    print("Test falliti: ",errori)