"""
-Closure Counter-
Define the function counter that returns 
a function that returns an increasing value.
The first value should be 1.

"""
def counter():
    cont = 0
    def function():
        nonlocal cont
        cont += 1
        return cont 
    return function

myContador_one = counter()
myContador_one()
myContador_one()
#myContador_two = counter()
#myContador_two()
print(myContador_one())
#print(myFunc())
        
    