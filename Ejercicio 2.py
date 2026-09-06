n = int(input("introduzca un número"))
b = int(input("introduzca el número de la base"))

k = ""

while n > 0:
    k = str(n % b) + k
    n = n // b

print(k)