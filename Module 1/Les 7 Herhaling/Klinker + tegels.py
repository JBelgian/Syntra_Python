import math

offertes = int(input("Hoeveel offertes moeten er gemaakt"))

for i in range(0, offertes):
    kent = input("Wat soort werk moet er gedaan? Klinkers? Tegels? Beide?")
    m2K = 0
    m2T = 0
    prijsKlinkers = 0
    prijsTegels = 0
    prijsWerk = 0
    kilometers = 0

    prijsTotaal = 0

    if kent == "Klinkers" or kent == "Beide":
        m2K = float(input("Hoeveel vierkante meter klinkers moeten er gelegd worden? "))
        keuzeKL = input("Welke klinkers? 10x10, 12x12 of 14x14? ")
        if keuzeKL == "10x10":
            prijsKlinkers = m2K * 14
        elif keuzeKL == "12x12":
            prijsKlinkers = m2K * 16
        elif keuzeKL == "14x14":
            prijsKlinkers = m2K * 16.5

    if kent == "Tegels" or kent == "Beide":
        m2T = float(input("Hoeveel vierkante meter tegels moeten er gelegd worden? "))
        keuzeT = input("Welke tegels? 60x60, 70x70, 80x80, of 100x100? ")
        if keuzeT == "60x60":
            prijsTegels = m2T * 26
        elif keuzeT == "70x70":
            prijsTegels = m2T * 28
        elif keuzeT == "80x80":
            prijsTegels = m2T * 32
        elif keuzeT == "100x100":
            prijsTegels = m2T * 35

    opbreek = input("Moeten er opgebroken worden eerst? ja of nee")

    if opbreek == "ja":
        werkUren = math.ceil(((m2K + m2T) / 12) + ((m2K + m2T) / 15))
        prijsWerk = werkUren * 40
    else:
        werkUren = math.ceil((m2K + m2T) / 12)
        prijsWerk = werkUren * 40

    kilometers = float(input("hoeveel km wordt afgelegd? "))

    if kilometers > 10:
        reisKosten = 5 + 0.30 * kilometers
    else:
        reisKosten = 5

    prijsTotaal = prijsWerk + prijsKlinkers + prijsTegels + reisKosten

    print("Klinkers kosten", prijsKlinkers, "euro")
    print("Tegels kosten", prijsTegels, "euro")
    print("Werk kosten zijn", prijsWerk, "euro")
    print("Totaal prijs bedraagt", prijsTotaal, "euro")
