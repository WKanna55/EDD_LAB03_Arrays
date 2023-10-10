#Ejercicio 02: Encontrar maximo y minimo de arreglo
#Complejidad de tiempo(n)
#Complejidad de espacio(1)

arreglo = [12,1,23,3,4]

maximo = -99999999
for i in arreglo:
    if i>maximo:
        maximo = i

print(maximo)