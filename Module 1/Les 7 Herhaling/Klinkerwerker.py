import math

m2 = float(input("Hoeveel vierkante meter klinkers moeten er gelegd worden? "))
keuze = input("Welke klinkers? 10x10, 12x12 of 14x14? ")
kilometers = float(input("hoeveel km wordt afgelegd? "))
opbreek = input("Moeten er opgebroken worden eerst? ja of nee")

prijsTotaal = 0

if keuze == "10x10":
    prijsKlinkers = m2 * 14
elif keuze == "12x12":
    prijsKlinkers = m2 * 16
elif keuze == "14x14":
    prijsKlinkers = m2 * 16.5

if opbreek == "ja":
    werkUren = math.ceil((m2 / 12) + (m2 / 15))
    prijsWerk = werkUren * 40
else:
    werkUren = math.ceil(m2 / 12)
    prijsWerk = werkUren * 40

if kilometers > 10:
    reisKosten = 5 + 0.30 * kilometers
else:
    reisKosten = 5

prijsTotaal = prijsWerk + prijsKlinkers + reisKosten

print("Klinkers kosten", prijsKlinkers, "euro")
print("Werk kosten zijn", prijsWerk, "euro")
print("Totaal prijs bedraagt", prijsTotaal, "euro")
