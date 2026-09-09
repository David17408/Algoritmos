n = int(input("Introduzca un número"))

resultado = 0
pos = 1

while n > 0:

    cifra = n % 10
    resultado += cifra * pos
    n //= 10

    if n > 0:

        pos *= 100

print(resultado)

