import random

getal1 = random.randint(1, 1000)
getal2 = random.randint(1, 1000)
getal3 = random.randint(1, 1000)

if getal1 > getal2 and getal1 > getal3:
    grootste = getal1
elif getal2 > getal1 and getal2 > getal3:
    grootste = getal2
else:
    grootste = getal3

print("Het grootste getal van de volgende getallen", getal1, getal2, getal3, "is", grootste)
