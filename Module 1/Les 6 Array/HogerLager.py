import random


score = 0
tries = 1
while score < tries:
    i = random.randint(1, 12)
    print(i)
    j = random.randint(1, 12)
    print(j)

    if i == j:
        j = random.randint(1,12)
    else:
        antwoord = input("hoger of lager?")
        if i < j and antwoord == "hoger":
            score = score + 1
            tries = tries + 1
        elif i > j and antwoord == "lager":
            score = score + 1
            tries = tries + 1
        else:
            tries = tries - 1
            print("Fout, uw score is", score)