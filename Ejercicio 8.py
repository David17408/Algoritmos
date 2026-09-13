while True:

    a = float(input("Longitúd del lado 1:"))
    b = float(input("Longitúd del lado 2:"))
    c = float(input("Longitúd del lado 3:"))

    #por lados#

    if a == b == c:
        print("El triángulo es equilátero") #Comprueba si los tres lados son iguales#

    elif a == b or b == c or a == c:

        print("El triángulo es isóseles") #Comprueba si al menos dos lados son iguales#

    else:

        print("El triángulo es escaleno") #En este caso todos los lados son distintos#

    #por ángulo#
    #Busca el mayor de los lados y toma los restantes#
    mayor = max(a,b,c)

    if mayor == a:
        x,y = b,c
    elif mayor == b:
        x,y = a,c
    else:
        x,y = a,b
    #Compara el cuadrado del lado mayor con los cuadrados de los otros lados y clasifica el triángulo#
    if mayor**2 == x**2+y**2:
        print("Rectángulo")
    elif mayor**2 < x**2+y**2:
        print("Acutángulo")
    else:
        print("Obtusángulo")
