"lo mismo que el codeInterview.py uno pero bien hecho"
objetivo = 13
lista = [2, 5, 8, 11]

def prueba(objetivo, lista):
    
    for i in lista:
        a = i
        for j in lista[::-1]:
            if a == j:
                break
            else:
                b = j
                if (a + b) == objetivo:
                    indices = [lista.index(a), lista.index(b)]
                    return indices
print(prueba(objetivo, lista))
        