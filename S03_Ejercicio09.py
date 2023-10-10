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
