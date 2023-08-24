import random
# tjeeeeena
# TODO: sdsd



trys = 10

ord = ["abc", "defghi", "jklm"]
ran = random.randrange(0,len(ord))
txt = "välkommen till hänga gubben, ordet har {} bokstäver"

print(txt.format(len(ord[ran])))
i = 0
while i < len(ord[ran]):
    print("___ ", end="")
    i += 1

