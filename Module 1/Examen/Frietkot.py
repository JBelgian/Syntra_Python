bestellingen = int(input("Voor hoeveel personen wordt er besteld? "))

def druk_afrekening(totaalPrijs):
    prijsEx = round(totaalPrijs / 121 * 100, 2)
    btw = round(totaalPrijs - prijsEx, 2)

    print("Prijs exl. BTW = ", prijsEx, "euro")
    print("BTW = ", btw, "euro")
    print("Totaal prijs = ", totaalPrijs, "euro")

for i in range(0, bestellingen):

    totaalPrijs = 0

    frieten = input("Welk soort frieten? A - kleine friet, B - middel friet, C - grote friet")

    if frieten == "A":
        totaalPrijs = 2.20
    elif frieten == "B":
        totaalPrijs = 2.50
    elif frieten == "C":
        totaalPrijs = 3

    extrasVraag = input("Wilt u extras? Ja of Nee ")
    if extrasVraag == "Ja":
        extras = input("Extras? A - speciaal, B - stoofvleessaus")

        if extras == "A":
            totaalPrijs = totaalPrijs + 1
        elif extras == "B":
            totaalPrijs = totaalPrijs + 1.80

    sausVraag = input("Wilt u saus? Ja of Nee ")
    if sausVraag == "Ja":
        saus = input("Hoe wilt u uw saus? A - op de frieten, B - klein bakje, C - groot bakje")
        if saus == "A" or saus == "B":
            totaalPrijs = totaalPrijs + 0.5
        elif saus == "C":
            totaalPrijs = totaalPrijs + 0.8

    snackVraag = input("Wilt u snack(s)? Ja of Nee ")
    if snackVraag == "Ja":
        snackQty = int(input("Hoeveel snacks wilt u?"))

        for j in range(0, snackQty):
            snack = input("Welke snack? A - Hamburger, boulet, mexicano, servola, B - nuggets, fingers, C - Bicky")
            if snack == "A":
                totaalPrijs = totaalPrijs + 2.30
            elif snack == "B":
                totaalPrijs = totaalPrijs + 2.50
            elif snack == "C":
                totaalPrijs = totaalPrijs + 3.20

    print(druk_afrekening(totaalPrijs))
