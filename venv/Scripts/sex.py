import random
# tjeeeeena
# TODO: sdsd



trys = 10

words = ["abc", "defghi", "jklm"]
ran = random.randrange(0,len(words))
txt = "välkommen till hänga gubben, ordet har {} bokstäver"
vald = words[ran]
alpha = list(vald)

print(txt.format(len(vald)))
i = 0
while i < len(vald):
    print("___ ", end="")
    i += 1

    
while trys>1:
    print(trys, " ", end="\n")
    guess = input("gissning: ")
    if guess.isdigit() or 1!=len(guess):
        print(vald, alpha)
    elif guess in alpha:
        continue
    else:
        trys-=1
