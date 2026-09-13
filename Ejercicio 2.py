n = int(input("introduzca un número"))
b = int(input("introduzca el número de la base"))

k = "" #lista que guarda los dígitos#

while n > 0:
    k = str(n % b) + k #Obtiene el residuo y lo coloca al inicio porque los dígitos se obtienen de derecha a izquierda
    n = n // b

print(k)
