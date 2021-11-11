"CoeWars2"
import math

print("escribe un numero: ")

n = int(input())
def squared_digits_series(n):
    sec=[]
    a = n
    u=1
    c=0
    i=n-1
    suma = 0
    while a != 0:
        c+=1
        residuo = 1%2

        if c>1:
            residuo = c%u
        if residuo!=0:#si entra es por que no es potencia de dos
            n = (u)*10 + 1 
            sec.append(n)
        else:
            u=c
            
            n = u*10+1
            sec.append(n)
        a-=1

        suma = sum(sec)
    return(suma)

Secuencia = squared_digits_series(n)
print(Secuencia)