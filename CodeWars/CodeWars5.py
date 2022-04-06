"Binary Addition"

print("enter a number")
a = int(input())
print("enter other number")
b = int(input())

def add_binary(a,b):
    c = a + b
    binario = format(c,"b")

    return(binario)
algo = add_binary(a,b)
print("\n" + algo)