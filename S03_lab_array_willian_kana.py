#Ejercicio 01: sumar los elementos de un arreglo
#complejidad de tiempo O(n)
#complejidad de espacio O(1)

arreglo = [1,2,3,4,5]
suma = 0
for i in arreglo:
    suma += i

print(suma)

#======================================================
#Ejercicio 02: Encontrar maximo y minimo de arreglo
#Complejidad de tiempo(n)
#Complejidad de espacio(1)

arreglo = [12,1,23,3,4]

maximo = -99999999
for i in arreglo:
    if i>maximo:
        maximo = i

print(maximo)

#======================================================
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

#======================================================
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

#======================================================
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

#======================================================
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

#======================================================
#Ejercicio 07: Matriz de multiplicacion
#Complejidad de tiempo O(3n) == O(n)
#Complejidad de espacio O(3n)

numero = 9
multiplicando = 1

matriz = [[0] * 3 for _ in range(numero)]

for i in range(numero):
    for j in range(3):
        if j == 0:
            matriz[i][j] = multiplicando
        elif j == 1:
            matriz[i][j] = numero
        else:
            matriz[i][j] = multiplicando*numero
    multiplicando += 1

for i in matriz:
    print(i)

#======================================================
#Ejercicio 08: Palabra mayor
#Complejidad de tiempo(n)
#Complejidad de espacio(1)

array = ["abc", "abcd", "abcdef", "ab", "ornamental"]

itemMayor= -1
for i in array:
    if len(i) > itemMayor:
        itemMayor = array.index(i)
       #print(i +" <--> " + j)
print(array[itemMayor])

#======================================================
#Ejercicio 09: Suma de matrices
#Complejidad de tiempo(n^2)
#Complejidad de espacio(n^2)

matriz1 =[[1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4]]
matriz2 =[[4,3,2,1],
          [4,3,2,1],
          [4,3,2,1],
          [4,3,2,1]]

matrizResultado=[[0]*4 for _ in range(len(matriz1))]

print(matrizResultado)

for i in range(len(matriz1)):
    for j in range(len(matriz1)):
        matrizResultado[i][j] = matriz1[i][j] + matriz2[i][j]

for i in matrizResultado:
    print(i)

#======================================================
#Ejercicio 10: Fibonacci con arreglos
#Complejidad de tiempo(n)
#Complejidad de espacio(n)

arreglo_fib = [0, 1]

n = 10

for i in range(n):
    siguiente = arreglo_fib[i] + arreglo_fib[i+1]
    arreglo_fib.append(siguiente)

print(arreglo_fib)

