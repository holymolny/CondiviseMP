from bancomat import *
from testMy import *

errori = 0

mainAdmin = Admin("admin1", "admin123")
secondAdmin = Admin("admin2", "admin123")
bancomat = Bancomat(mainAdmin, 500, 1000)

#Test login admin

errori += testEqual(1, bancomat.login("admin1", "admin123",True), True)
errori += testEqual(2, bancomat.login("admin1", "admin2",True), False)
errori += testEqual(3, bancomat.login("admin1", "admin123",False), True)

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

try:
    adminx = Admin("adminx", "a1")
    errori += 1
    print(f"Test {11}: Failed")
except ValueError:
    pass

#Test aggiunta/modifica utenti
errori += testEqual(12, bancomat.aggiungi_utente("admin1", "admin123",cliente1,1000), True)
errori += testEqual(13, bancomat.aggiungi_utente("admin1", "admin123",cliente1,1000), False)
errori += testEqual(14, bancomat.aggiungi_utente("admin1", "admin123",cliente2), True)
errori += testEqual(15, bancomat.aggiungi_utente("admin1", "admin123",cliente3,500), True)
errori += testEqual(16, bancomat.aggiungi_utente("admin1", "admin123",cliente4,1500), True)
errori += testEqual(17, bancomat.aggiungi_utente("admin1", "admin123",secondAdmin,1000), False)
errori += testEqual(18, bancomat.aggiungi_utente("admin1", "admin123",secondAdmin,0), True)
errori += testEqual(19, bancomat.get_lista_utenti("admin1", "admin123"), [mainAdmin, cliente1, cliente2, cliente3, cliente4, secondAdmin])
errori += testEqual(20, bancomat.get_utente("admin1", "admin123","cl1"), cliente1)
errori += testEqual(21, bancomat.get_utente("admin1", "admin123","clx"), None)
errori += testEqual(22, bancomat.rimuovi_utente("admin1", "admin123","cl1"), True)
errori += testEqual(23, bancomat.get_utente("admin1", "admin123","cl1"), None)
errori += testEqual(24, bancomat.modifica_somma("admin1", "admin123","cl3", 1000), True)
errori += testEqual(25, bancomat.get_saldo("cl3", "111111"), 1000)
errori += testEqual(26, bancomat.modifica_pin("cl2", "000000", "123456"), True)
errori += testEqual(27, bancomat.aggiungi_utente("admin1", "admin123",cliente1,1000), True)

#Test login clienti
errori += testEqual(28, bancomat.login("cl2", "123456",False), True)
errori += testEqual(29, bancomat.login("cl2", "000001",False), False)
errori += testEqual(30, bancomat.login("cl2", "123456",True), False)

#Test sul conto corrente
errori += testEqual(31, bancomat.preleva("cl2", "123456", 100), (True,"")) #-100
errori += testEqual(32, bancomat.preleva("cl2", "123456", 2000), (False, Bancomat.LIMITE_PRELIEVO_SUPERATO))
errori += testEqual(33, bancomat.preleva("cl2", "123456", 500), (False, Bancomat.FONDI_INSUFFICIENTI))
errori += testEqual(34, bancomat.preleva("cl2", "123455", 100), (False, Bancomat.LOGIN_ERRATO))
errori += testEqual(35, bancomat.deposita("cl2", "123456", 1000), (True,"")) #900
errori += testEqual(36, bancomat.preleva("cl2", "123456", 500), (True, "")) #400
errori += testEqual(37, bancomat.trasferisci("cl2", "123456", "cl3", 500), (True,"")) #-100
errori += testEqual(38, bancomat.trasferisci("cl2", "123456", "admin1", 1), (False, Bancomat.UTENTE_NON_VALIDO))
errori += testEqual(39, bancomat.trasferisci("cl2", "123456", "cl3", 500), (False, Bancomat.FONDI_INSUFFICIENTI))
errori += testEqual(40, bancomat.get_saldo("cl2", "123456"), -100)
errori += testEqual(41, bancomat.deposita("admin1", "admin123", 1000), (False, Bancomat.UTENTE_NON_VALIDO)) #admin non può cambiare il saldo
errori += testEqual(42, bancomat.preleva("admin1", "admin123", 100), (False, Bancomat.UTENTE_NON_VALIDO)) #admin non può cambiare il saldo

#Test su liste
errori += testEqual(43, bancomat.lista_clienti_con_saldo_negativo("admin1", "admin123"),[cliente2])
errori += testEqual(44, bancomat.deposita("cl2", "123456", 100), (True,"")) #0
errori += testEqual(45, bancomat.lista_clienti_con_saldo_negativo("admin1", "admin123"),[])
errori += testEqual(46, bancomat.lista_clienti_con_saldo_almeno("admin2", "admin123",0),[cliente2, cliente3, cliente4,cliente1])
errori += testEqual(47, bancomat.lista_clienti_con_saldo_almeno("admin2", "admin123",1001),[cliente3,cliente4])
errori += testEqual(48, bancomat.lista_clienti_con_saldo_almeno("admin3", "admin123",1000),None)

#Test su file e uguaglianza
errori += testEqual(49, bancomat.carica_da_file("admin1", "admin123","bancomat123.txt"), False)
errori += testEqual(50, bancomat.salva_su_file("admin1", "admin123","bancomat.txt"), True)
bancomat2 = Bancomat(secondAdmin, 100, 500)
errori += testEqual(51, (bancomat == bancomat2), False)
errori += testEqual(52, bancomat2.carica_da_file("admin2", "admin123","bancomat.txt"), True)
errori += testEqual(53, bancomat, bancomat2)

bancomat2 = Bancomat(secondAdmin, 500, 1000)
bancomat2.aggiungi_utente("admin2", "admin123",cliente2,0)
bancomat2.aggiungi_utente("admin2", "admin123",cliente1,1000)
bancomat2.aggiungi_utente("admin2", "admin123",mainAdmin,0)
bancomat2.aggiungi_utente("admin2", "admin123",cliente4,1500)
bancomat2.aggiungi_utente("admin2", "admin123",cliente3,1500)
errori += testEqual(54, bancomat, bancomat2)

clientex = Cliente("clx", "123456", "exit()", "Rossi")
bancomat2.aggiungi_utente("admin2", "admin123",clientex,1500)
errori += testEqual(55, bancomat2.salva_su_file("admin1", "admin123","bancomat2.txt"), True)
errori += testEqual(56, bancomat2.carica_da_file("admin2", "admin123","bancomat2.txt"), True)

#stampa finale
print("==========> Stampa finale")

# abbiamo finito ?
if errori == 0:
    print(bancomat)
    print("\t****Test completati -- effettuare la consegna come da README")
else:
    print("Test falliti: ",errori)