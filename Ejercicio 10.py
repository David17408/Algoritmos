n = int(input("Introduzca un número: "))

cantidad = 0
mayor = 0

for num in range(2, n + 1):

    primo = True

    divisor = 2

    while divisor**2 <= num:

        if num % divisor == 0:

            primo = False

        divisor = divisor + 1

    if primo:

        print(num)
        cantidad = cantidad + 1
        mayor = num

print("Cantidad de primos:", cantidad)
print("Mayor primo:", mayor)