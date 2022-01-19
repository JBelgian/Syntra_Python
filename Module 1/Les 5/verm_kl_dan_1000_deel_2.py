getal = int(input("Geef een getal in "))
end = int(input("Geef een eind getal in "))
teller = 0
product = 0

if end > getal:
    while product < end:
        product = getal * teller
        teller = teller + 1
        if product < end:
            print(product)
else:
    print("Eind getal was kleiner dan getal")
