def findSmall(getal1,getal2):
    if getal1 < getal2:
        return getal1
    elif getal2 < getal1:
        return getal2
    else:
        return "Getallen zijn gelijk"

print(findSmall(2,7))
print(findSmall(2,2))
print(findSmall(4,7))
print(findSmall(7,2))
print(findSmall(3,3))

