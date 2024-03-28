from bancomat import *
from testMy import *

#Registra se ci sono errori
errori = 0

mainAdmin = Admin("admin1", "admin123")
secondAdmin = Admin("admin2", "admin123")
bancomat = Bancomat(mainAdmin, 500, 1000)

#print(mainAdmin, secondAdmin, bancomat)

#Test login admin
print("Errore 1:")
errori += testEqual(1, bancomat.login("admin1", "admin123",True), True)
print("Errore 2:")
errori += testEqual(2, bancomat.login("admin1", "admin2",True), False)
print("Errore 3:")
errori += testEqual(3, bancomat.login("admin1", "admin123",False), True)

print(bancomat.login("admin1", "admin123",False))

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

#Da chiedere al professore
#Non genera eccezione ma non la deve generare perchè i dati in input sono corretti
try:
    adminx = Admin("adminx", "a1")
    errori += 1
    print(f"Test {11}: Failed")
except ValueError:
    pass


#Stampa se ci sono errori
# abbiamo finito ?
if errori == 0:
    print(bancomat)
    print("\t****Test completati -- effettuare la consegna come da README")
else:
    print("Test falliti: ",errori)