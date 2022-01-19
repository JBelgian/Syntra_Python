lijstOutput = []
dagTotaal = 0
naamKlant = input("Wat is de naam van volgende klant? ")

while not naamKlant == "stop":
    totaalPrijs = 0
    prijs = 0
    pakket = input("Welk pakket? Basic, Bio, Luxe, Superluxe ")
    if pakket == "Basic":
        prijs = 8
    elif pakket == "Bio":
        prijs = 10
    elif pakket == "Luxe":
        prijs = 12
    elif pakket == "Superluxe":
        prijs = 15

    extrasVraag = input("Wilt u extras? Ja of Nee? ")
    prijsExtra = 0
    extraDescr = ""
    while extrasVraag == "Ja":
        extras = input("Welke extras? Polish, Wax, Winterproof, Stofzuiger ")
        if extras == "Polish":
            prijsExtra = prijsExtra + 3
            extraDescr = (extraDescr, extras)
            extrasVraag = input("Wilt u meer extras? Ja of Nee? ")
        elif extras == "Wax":
            prijsExtra = prijsExtra + 2.80
            extraDescr = (extraDescr, extras)
            extrasVraag = input("Wilt u meer extras? Ja of Nee? ")
        elif extras == "Winterproof":
            prijsExtra = prijsExtra + 2.50
            extraDescr = (extraDescr, extras)
            extrasVraag = input("Wilt u meer extras? Ja of Nee? ")
        elif extras == "Stofzuiger":
            prijsExtra = prijsExtra + 2
            extraDescr = (extraDescr, extras)
            extrasVraag = input("Wilt u meer extras? Ja of Nee? ")

    totaalPrijs = prijs + prijsExtra
    lijstInput = (naamKlant, pakket, extraDescr, totaalPrijs)
    lijstOutput.append(lijstInput)
    dagTotaal = dagTotaal + totaalPrijs
    naamKlant = input("Wat is de naam van volgende klant? (of 'stop' om te beeindigen) ")

print(lijstOutput)
print("Dagtotaal bedraagt", dagTotaal, "euro")
