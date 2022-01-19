import random

getal1 = random.randint(1, 100)
getal2 = random.randint(1, 100)
getal3 = random.randint(1, 100)

if getal1 < getal2 and getal1 < getal3:
    kleinste = getal1
elif getal2 < getal1 and getal2 < getal3:
    kleinste = getal2
else:
    kleinste = getal3

print("Het kleinste getal van de volgende getallen", getal1, getal2, getal3, "is", kleinste)
