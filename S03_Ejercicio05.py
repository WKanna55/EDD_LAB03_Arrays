#Ejercicio 05: Ordenamiento de un arreglo
#Complejidad de tiempo(n^2)
#Complejidad de espacio(n)

arreglo = [2,6,7,1,9,10,11]

for i in range(len(arreglo)):
    for j in range(0, len(arreglo)-i-1):
        if arreglo[j] > arreglo[j+1]:
            temp = arreglo[j]
            arreglo[j]= arreglo[j+1]
            arreglo[j+1] = temp

print(arreglo)
