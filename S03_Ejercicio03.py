#Ejercicio 03: Contar pares e impares de arreglos
#Complejidad de tiempo(n)
#Complejidad de espacio(1)

arreglo = [1,2,3,4,5,6,7]
pares = 0
impares = 0
for i in arreglo:
    if i % 2 == 0:
        pares+=1
    else:
        impares+=1

print("pares = " + str(pares))
print("impares = " + str(impares))


