#Ejercicio 03: Eliminar duplicados
#Complejidad de tiempo O(n)
#Complejidad de espacio O(n)

arreglo = [1,2,3,4,5,6,6,5,4]
arreglosd =[]
contador = 0
for i in arreglo:
    if i not in arreglosd:
        arreglosd.append(i)

print(arreglosd)
