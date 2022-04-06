def tribonacci(signature, n):
    c = n
    l = len(signature)
    if c==0:
        signature.clear()
        return signature
    if c<=len(signature):
        return signature[:c]
    else:    
        while c>0:
            suma = 0
            for i in signature[-l:]:
                suma +=i
            signature.append(suma)
            c -= 1
        return(signature[:n])
print(tribonacci([0,0,0,0,1],10))