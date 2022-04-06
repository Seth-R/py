"Kata: Jaden Casing Strings"

print("write someting: ")
string = input()

def to_jaden_case(string):
    lista = string.split()
    i = 0
    p=0
    palabra = []
    for palabras in lista:
        
        palabra[:0] = palabras
        for letra in palabra:
            i+=1
            if i == 1:
                letra = letra.upper()
                palabra[0] = letra
                lista[p] = "".join(palabra)
            i-=1
            p+=1
            palabra.clear()
                
    return(" ".join(lista))


print(to_jaden_case(string))