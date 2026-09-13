n = int(input("Introduzca un número"))

resultado = 0
pos = 1

while n > 0: #Repite mientras queden cifras por procesae

    cifra = n % 10 #Obtiene la última cifra#
    resultado += cifra * pos #Añade la cifra multiplicada por su posición#
    n //= 10 #Elimina la última cifra#

    #Si quedan cifras aumenta la posición dos lugares#
    if n > 0:

        pos *= 100

print(resultado)

