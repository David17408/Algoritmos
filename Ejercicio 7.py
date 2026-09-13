n = int(input("Introduzca el número de datos: "))

datos = [] #Crea una lista#

for i in range(n): #Repite el proceso#

    x = int(input("Introduzca un número: "))
    datos.append (x) #Guarda los números introducidos#

mayor = 0
moda = 0
#Recorre cada elemento de la lista#
for x in datos:

    frecuencia = 0
    #Compara x con los elementos de la lista#
    for y in datos:

        if x == y: #Calcula la frecuencia comparandolo con cada dato y la aumenta en 1 cuando encuentra el mismo dato repetido#

            frecuencia = frecuencia + 1
    #Si x aparece más veces que cualquier elemento anterior actualiza la mayor frecuencia encontrada#
    if frecuencia > mayor:
    
        mayor = frecuencia
        modas = [x] #Crea una lista con la moda#

    elif frecuencia == mayor: #Si x tiene la misma frecuencia que la máxima encontrada la añade a la lista#

        modas.append(x)

if mayor == 1: #Si todos los datos aparecen solo una vez#

    print ("No hay moda")

else: #Cuando algun dato aparece más de una vez#

    print (f"La moda es:", modas)
