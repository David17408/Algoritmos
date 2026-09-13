import math

t = float(input("Ingrese la tolerancia"))

suma = 0
n = 0
termino = 1

while abs(termino) >= t: #Continúa mientras el término sea mayor a la tolerancia#
#Usa la serie de leibniz para la aproximación#
    termino = ((-1)**n)/(2*n + 1) 

    suma += termino
    n += 1

aprox = suma*4
error = abs(math.pi - aprox) #Calcula el error#

print(f"El valor aproximado de pi es: ", aprox)
print(f"El error es: ", error)
