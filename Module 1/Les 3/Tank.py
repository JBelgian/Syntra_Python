basis = float(input("Geef basis in"))
hoogte = float(input("Geef hoogte in"))
diepte = float(input("Geef diepte in"))
ppl = 0.38
kostprijs = basis * hoogte * diepte * ppl
print("De prijs voor de tank te vullen is",round(kostprijs,2))