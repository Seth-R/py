"Deoxyribonucleic acid (DNA) is a chemical found in "
"the nucleus of cells and carries the \"instructions" 
"for the development and functioning of living organisms."
"If you want to know more: http://en.wikipedia.org/wiki/DNA"
"In DNA strings, symbols \"A"" and \"T" "are complements of each other,"
"as \"C" "and \"G"". You have function with one side of the DNA "
"(string, except for Haskell); you need to get the other complementary side."
" DNA strand is never empty or there is no DNA at all (again, except for Haskell)."
"More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)"
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