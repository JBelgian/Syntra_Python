getal = int(input("Geef je getal in "))
kleinste = getal
for i in range(1, 10):
    getal = int(input("Geef je getal in "))
    if getal < kleinste:
        kleinste = getal
print(kleinste)
