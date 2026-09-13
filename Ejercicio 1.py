import math

opcion = 0

while opcion != 4: #Repite el menú hasta que elija salir#
    print("Introduzca el número de la opción")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Salir")
    opcion = int(input("Ingrese la opcion:"))
    
    if (opcion == 1): 
        print("Esta cosa calcula la serie de Taylor del seno =)")

        #Convierte los grados a radianes#
        grados = float(input("Introduzca el valor en grados:"))
        
        n = int(input("Introduzca el numero de terminos"))
        
        x = (grados * math.pi)/180
        
        seno = 0
        #Calcula el seno usando la serie de Taylor#
        for k in range (n):
        
            seno +=(((-1)**k)*x**(2*k+1))/math.factorial(2*k+1)
        
        print(seno)
        
    elif (opcion == 2):
        
        print("Esta cosa calcula la serie de Taylor del coseno =)")
        
         #Convierte los grados a radianes#
        grados = float(input("Introduzca el valor en grados:"))
        
        n = int(input("Introduzca el numero de terminos"))
        
        x = (grados * math.pi)/180
        
        coseno = 0

        #Calcula el coseno usando la serie de Taylor#
        for k in range (n):
        
            coseno += (((-1)**n)*(x**(2*n)))/math.factorial(2*n)
        
        print(coseno)

    elif (opcion == 3):
        print("No se hace :3c")
    elif (opcion == 4): #Finaliza el proceso#
        print("cualquier cosa")

else: #En caso de seleccionar una opción que no este, indicará que la opción es incorrecta#
    print("opcion incorrecta")
