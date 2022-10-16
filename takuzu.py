import lib

matrice = lib.initTakuzuNonCorrect()

check = lib.checkValidity(matrice)

lib.resolveTakuzu(matrice)

print(matrice)
print(check)