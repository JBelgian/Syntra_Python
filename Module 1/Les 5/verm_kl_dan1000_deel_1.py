getal = int(input("Geef een getal in "))
teller = 0
product = 0
while product < 1000:
    product = getal * teller
    teller = teller + 1
    if product < 1000:
        print(product)
