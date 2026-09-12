#sin listas#

n = int(input("Introduzca el número de datos: "))

suma = 0
suma2 = 0

for i in range (n):

    x = float(input("Introduzca el dato: "))

    suma = suma + x
    suma2 = suma2 + x**2

    prom = suma / n

desv = ((suma2 - n*prom**2)/n)**0.5
desv2 = ((suma2 - n*prom**2)/(n-1))**0.5

print(f"La desviación estándar muestral es:", desv)
print(f"La desviación estándar muestral es:", desv2)