n = int(input("Introduzca el número de datos: "))

datos = [] #Crea una lista#

for i in range (n): #Repite n veces para ingresar todos los datos#

    x = float(input("Ingrese los datos:")) #Agrega el dato a la lista#
    datos.append(x)

prom = sum(datos)/n #Calcula el promedio de los datos#

suma = 0

for x in (datos): #Recorre todos los datos de la lista#
    
    suma = suma + (x - prom)**2 #Hace el numerador de las formulas de desviación#

#Calcula las desviaciones#
desv = (suma / n)**(0.5)
desv2 = (suma / (n-1))**(0.5)

print(f"La desviación estándar muestral es:", desv)
print(f"La desviación estándar poblacional es:", desv2)

