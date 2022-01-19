product = ""
prijs = ""
totaal = 0

while not product == "betaal":
    product = input("Geef een product in? ")
    if product == "betaal":
        break
    else:
        try:
            prijs = float(input("Geef een prijs in? "))
            totaal = totaal + prijs
        except ValueError:
            print("Gelieve een getal als prijs in te geven")

print("Het totaal bedrag is", totaal)
