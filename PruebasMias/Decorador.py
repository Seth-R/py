def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador#el decorador encapsula la funcion en el que se encuentre
def suma(a, b):
    print("Entra en funcion suma")
    return a + b


print(suma(5,8))

