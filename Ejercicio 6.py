n = int(input("Introduzca el número de datos: "))

datos = []

for i in range (n):

    x = float(input("Ingrese los datos:"))
    datos.append(x)

prom = sum(datos)/n

suma = 0

for x in (datos):

    suma = suma + (x - prom)**2

desv = (suma / n)**(0.5)
desv2 = (suma / (n-1))**(0.5)

print(f"La desviación estándar muestral es:", desv)
print(f"La desviación estándar poblacional es:", desv2)

