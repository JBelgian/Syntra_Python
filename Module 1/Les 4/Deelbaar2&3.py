import random

getal = random.randint(0, 100)

mod2 = getal % 2
mod3 = getal % 3

if mod2 == 0 and mod3 == 0:
    print(getal, "is deelbaar door 2 en 3")
else:
    print(getal, "is niet deelbaar door 2 en 3")
