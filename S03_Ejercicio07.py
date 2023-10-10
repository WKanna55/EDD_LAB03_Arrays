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
