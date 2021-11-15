print("write someting: ")
sentence = input()

def get_count(sentence):
    vowel = 0
    for vocal in sentence:
        if vocal.lower() == "a" or vocal.lower() == "e" or vocal.lower() == "i" or vocal.lower() == "o" or vocal.lower() == "u":
            vowel+=1
    return(vowel)

vocal = get_count(sentence)
print(vocal)