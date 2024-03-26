def testEqual(ntest, x, y):
    """ Controlla se x e y sono uguali e restituisce 1 se non lo sono e
    0 se lo sono"""
    if x == y:
        return 0
    else:
        print(f"Test {ntest}: Failed")
        return 1