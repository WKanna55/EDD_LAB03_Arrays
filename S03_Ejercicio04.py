#Ejercicio 04: Busqueda de un elemento
#Complejidad de tiempo(n)
#Complejidad de espacio(1)

arreglo = [1,5,6,3,11,2,55]

n = 55

for i in arreglo:
    if i == n:
        print("Numero encontrado")
    elif i != n and arreglo.index(i)== len(arreglo)-1:
        print("No se encontro el numero")