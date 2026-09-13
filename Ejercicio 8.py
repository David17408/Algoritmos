while True:

    a = float(input("Longitúd del lado 1:"))
    b = float(input("Longitúd del lado 2:"))
    c = float(input("Longitúd del lado 3:"))

    #por lados#

    if a == b == c:
        print("El triángulo es equilátero")

    elif a == b or b == c or a == c:

        print("El triángulo es isóseles")

    else:

        print("El triángulo es escaleno")

    #por ángulo#

    mayor = max(a,b,c)

    if mayor == a:
        x,y = b,c
    elif mayor == b:
        x,y = a,c
    else:
        x,y = a,b

    if mayor**2 == x**2+y**2:
        print("Rectángulo")
    elif mayor**2 < x**2+y**2:
        print("Acutángulo")
    else:
        print("Obtusángulo")