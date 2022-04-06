LlegaAlgo = ["algo", "a", "a", "b"]

def NombreDeMetodo(LlegaAlgo):

    return{i:LlegaAlgo.count(i) for  i in LlegaAlgo}

resultado = NombreDeMetodo(LlegaAlgo)

print(resultado)