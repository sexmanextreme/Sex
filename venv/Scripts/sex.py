import random

# tjeeeeena
# TODO: sdsd


trys = 10
ans = 0

words = ["aaaf", "defghh", "jkkml"]
ran = random.randrange(0, len(words))
txt = "välkommen till hänga gubben, ordet har {} bokstäver"
vald = words[ran]
alpha = list(vald)
svar = [None] * len(vald)

print(txt.format(len(vald)))


def sex(guess):
    for i in range(len(vald)):
        if guess not in alpha[i] or guess == str() or svar[i] is None:
            svar[i] = "___"
            i += 1

        else:
            svar[i] = guess
            i += 1

    print(svar)


while trys > 1 or ans != len(vald):

    print(trys, " ", end="\n")

    guess = input("gissning: ")

    print(vald, alpha)

    if guess.isdigit() or 1 != len(guess):
        print("snälla använd endast 1 bokstav och inga siffror")

    elif guess in alpha:
        ans += 1
        sex(guess)

    else:
        trys -= 1


'''
while pouyan == gay in bed[]
    pouyan += dick
    pouyan -= dick
'''
