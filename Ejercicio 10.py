n = int(input("Introduzca un número: "))

cantidad = 0
mayor = 0

for num in range(2, n + 1):  #Recorre los números desde 2 hasta n##

    primo = True

    divisor = 2 

    while divisor**2 <= num: #Prueba divisores hasta la raiz cuadrada de num#
    
        #Comprueba si num es divisible entre divisor#
        if num % divisor == 0: 
            primo = False

        divisor = divisor + 1
    #Si no encuentra divisores el número es primo#
    if primo:

        print(num)
        cantidad = cantidad + 1
        mayor = num #Actualiza al mayor primo encontrado#

print("Cantidad de primos:", cantidad)
print("Mayor primo:", mayor)
