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
