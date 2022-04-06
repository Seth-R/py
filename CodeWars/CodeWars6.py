"Complementary DNA"
dna = "AATTGC"
def DNA_strand(dna):
    c=0
    adn = []
    for letra in dna:
        adn[:0] = letra
    for cells in adn:
        cells
        if cells.upper() == "A":
            adn[c] = "T"
            c+=1
        if  cells.upper() == "T":
            adn[c] = "A"
            c+=1
        if cells.upper() == "G":
            adn[c] = "C"
            c+=1
        if cells.upper() == "C":
            adn[c] = "G"
            c+=1
    return "".join(list(reversed(adn)))

print (DNA_strand(dna))