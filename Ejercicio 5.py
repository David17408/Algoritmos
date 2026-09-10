A = []

num = int(input("Número de elementos: "))

for _ in range(num):
        A.append(int(input("elemento?: ")))

pares = [x for x in A if x % 2 == 0]

print(A)
print(pares)

prompar = sum(pares) / len(pares)

if num != 0:
    print(f"El promedio de los pares es: {prompar}")

else:
    print("No hay pares")
