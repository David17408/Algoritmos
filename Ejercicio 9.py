import math

t = float(input("Ingrese la tolerancia"))

suma = 0
n = 0
termino = 1

while abs(termino) >= t:

    termino = ((-1)**n)/(2*n + 1)

    suma += termino
    n += 1

aprox = suma*4
error = abs(math.pi - aprox)

print(f"El valor aproximado de pi es: ", aprox)
print(f"El error es: ", error)