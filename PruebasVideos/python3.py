#print("agrga algo a una lista (usando como separadores ',')")

#lista = input().split(',')

#print(lista)
lista2 = []

print("si ya no desea colocar mas elementos a la lista ponga una 'n' ")
algo = input()
while algo != 'n':
    lista2 += [algo]
    print("desea seguir agregando?")
    algo = input()

print(lista2)    
    
