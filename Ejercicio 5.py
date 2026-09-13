A = [] #Se crea la lista#

num = int(input("Número de elementos: "))

for _ in range(num): #Se introducen los elementos#
        A.append(int(input("elemento?: ")))

pares = [x for x in A if x % 2 == 0] #Lista con los pares#

print(A)
print(pares)

prompar = sum(pares) / len(pares) #Promedia los pares#

print(f"El promedio de pares es: ", prompar)
