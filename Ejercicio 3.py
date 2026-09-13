frase = input("Introduzca una frase:")

palabras = frase.split() #Separa en palabras#

inv_palabra = palabras[::-1] #Invierte el orden de las palabras#

inv_letras = frase[::-1] #Invierte el orden de las letras#

print(inv_letras)
print(inv_palabra)
