"crea un codigo que te cuente cuantas veces se repite una letra ejemplo:"
"si escribes 'aabba' el resultado seria se repiten 3 'a' y 2 'b'"

print ("escribe algo: ")

lista = input()

def contarElementosLista(lista):
    """
    Recibe una lista, y devuelve un diccionario con todas las repeticiones de
    cada valor
    """
    #i es un contador y lista.count(i) va contando cuantas veces se repite el indice
    
    return {i:lista.count(i) for i in lista}

 #{i:lista.count(i), i:lista.count(i), i:lista.count(i)} for i in lista
#{"a": , "b" , "c": }
resultado=contarElementosLista(lista) # {'a': 3, 'b': 1, 'c': 3}
print (resultado)


#print (lista)