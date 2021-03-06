"""
kata of 6 kyu
If you have completed the Tribonacci sequence kata, you would know by now that mister Fibonacci 
has at least a bigger brother. If not, give it a quick look to get how things work.

Well, time to expand the family a little more: think of a Quadribonacci starting with a signature of 
4 elements and each following element is the sum of the 4 previous, a Pentabonacci (well Cinquebonacci would probably 
sound a bit more italian, but it would also sound really awful) with a signature of 5 elements and each following
 element is the sum of the 5 previous, and so on.

Well, guess what? You have to build a Xbonacci function that takes a signature of X elements - and remember each next 
element is the sum of the last X elements - and returns the first n elements of the so seeded sequence.  
"""

#numero = input("escribe un numero: ")
#diccionary = [1, 2, 3]
#numero = 10
def tribonacci(signature, n):
    c = n
    if c==0:
        signature.clear()
        return signature
    if c<=len(signature):
        return signature[:c]
    else:    
        while c>0:
            suma = 0
            for i in signature[-3:]:
                suma +=i
            signature.append(suma)
            c -= 1
        return(signature[:n])
print(tribonacci([0.5, 0.5, 0.5], 0))