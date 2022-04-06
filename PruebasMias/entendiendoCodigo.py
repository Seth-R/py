
algo = []
algo = input("escribe algo:")

diccionario = {}
for i in algo:
    diccionario.update({i:algo.count(i) for i in algo})       
print(diccionario)