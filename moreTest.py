from bancomat import *
from testMy import *

mainAdmin = Admin("admin1", "admin123")
secondAdmin = Admin("admin2", "admin123")
bancomat = Bancomat(mainAdmin, 500, 1000)

print(mainAdmin, secondAdmin, bancomat)