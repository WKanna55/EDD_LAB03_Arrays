#Ejercicio 10: Fibonacci con arreglos
#Complejidad de tiempo(n)
#Complejidad de espacio(n)

arreglo_fib = [0, 1]

n = 10

for i in range(n):
    siguiente = arreglo_fib[i] + arreglo_fib[i+1]
    arreglo_fib.append(siguiente)

print(arreglo_fib)
