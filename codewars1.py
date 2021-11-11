print("write something: ")

cc = input()
l = ""
letras=[]
def maskify(cc):
    count = 0
    for i in cc:
        count+=1
        letras.append(i)

    if count>4:
        sharp = count-4
        for i in range(len(letras[:sharp])):
            letras[i] = "#"

    let = "".join(letras)
    
    return(let)


print (maskify(cc))
    