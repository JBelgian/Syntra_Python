import random

getal = random.randint(1, 100)
aantal = 0
kleiner = 0
tussen = 0
groter = 0

while aantal < 10:
    if getal < 30:
        kleiner = kleiner + 1
        aantal = aantal + 1
        print(getal)
    if getal < 60:
        tussen = tussen + 1
        aantal = aantal + 1
        print(getal)
    if getal > 60:
        groter = groter + 1
        aantal = aantal + 1
        print(getal)

print(kleiner, "zijn < 30")
print(tussen, "zijn 30 < 60")
print(groter, "zijn > 60")
