"Kata: Convert string to camel case"


def to_camel_case(text):
    camelCase = "-_"
    letra = text

    for guion in range(len(camelCase)):
        letra = letra.replace(camelCase[guion], "")

    
    #    str(guion.upper())

    return letra
print(to_camel_case(text="the_stealth_warrior"))