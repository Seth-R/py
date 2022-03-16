"two sum regresar las dos posisiones de la lista que de esos dos"
"numeros sumados te den el numero objetivo"
#print("escoje numero objetivo: ")
#objetivo = int(input())
lista = [2,5,8,11]
objetivo = 10
a = 0
b=0
sum = 0
algo = []
for i in lista:
    a = i
    b += lista.index(i)
    if a <= objetivo:
        sum += a
        objetivo -= a
        algo += [lista.index(i)]
        if objetivo > 0 and b>0:
            sum -= a
            objetivo += a
            algo.pop(lista.index(i))


    
    
print(algo)

