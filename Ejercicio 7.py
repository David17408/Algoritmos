n = int(input("Introduzca el número de datos: "))

datos = []

for i in range(n):

    x = int(input("Introduzca un número: "))
    datos.append (x)

mayor = 0
moda = 0

for x in datos:

    frecuencia = 0

    for y in datos:

        if x == y:

            frecuencia = frecuencia + 1

    if frecuencia > mayor:

        mayor = frecuencia
        modas = [x]

    elif frecuencia == mayor:

        modas.append(x)

if mayor == 1:

    print ("No hay moda")

else:

    print (f"La moda es:", modas)