"kata 7kyu: Alphabetical Grid"
# Task:
# You need to write a function grid that returns an alphabetical grid of size NxN, where a = 0, b = 1, c = 2....
# Examples:
"grid(4)"
# a b c d
# b c d e
# c d e f
# d e f g
#--->N = N+N-1
"grid(10)"
# a b c d e f g h i j
# b c d e f g h i j k
# c d e f g h i j k l
# d e f g h i j k l m
# e f g h i j k l m n
# f g h i j k l m n o
# g h i j k l m n o p
# h i j k l m n o p q
# i j k l m n o p q r
# j k l m n o p q r s
import string

# def listAlphabet():
#       return [chr(i) for i in range(ord('a'),ord('z')+1)]
# print(listAlphabet())
def grid(N):
    if N >= 0:
        #R = "" 
        grid = ""
        a = N+N-1
        abecedario = list(map(chr, range(97, 123)))
        while len(abecedario) < a:
            abecedario += abecedario
        
        copia = abecedario  
        #return copia
        for i in range(len(copia[a:])):
            copia.pop()
        #return copia
        c = N
        while N > 0:
            if N>1:  
                grid += (" ").join(copia[:c]) + "\n"
                copia+=[copia.pop(0)]
                N-=1
            else:
                grid += (" ").join(copia[:c])
                copia+=[copia.pop(0)]
                N-=1
        return grid
    else:
        return None
#algo = "asdfg" + "\n" +"algo mas"

print(grid(N = 4))



