"Implement a function that adds two numbers together and returns their sum in binary."
"The conversion can be done before, or after the addition."
"The binary number returned should be a string."

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