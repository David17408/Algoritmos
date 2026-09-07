f=input("Introduzca una función:")
a=float(input("Límite inferior"))
b=float(input("Límite superior"))
n=int(input("Número de subintervalos"))

delta_x = (b-a)/n
suma = 0

for i in range(n):
    x = (a+i*delta_x)
    y = eval(f)
    suma = suma + y*delta_x
print(suma)