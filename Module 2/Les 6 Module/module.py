import math


def opp_driehoek(basis, hoogte):
    opp = (basis * hoogte / 2)
    print("De oppervlakte van een driehoek met basis ", basis, "en hoogte ", hoogte, "is gelijk aan ", opp)


def omtrek_driehoek(z1, z2, z3):
    omtr = z1 + z2 + z3
    print("De omtrek van een driehoek met zijdes van ", z1, z2, z3, "is gelijk aan ", omtr)


def opp_vierkant(basis, hoogte):
    opp = basis * hoogte
    print("De oppervlakte van een vierkant met basis ", basis, "en hoogte ", hoogte, "is gelijk aan ", opp)


def omtrek_vierkant(basis, hoogte):
    omtr = ((basis + hoogte) * 2)
    print("De omtrek van een vierkant met basis ", basis, "en hoogte ", hoogte, "is gelijk aan ", omtr)


def opp_rechthoek(basis, hoogte):
    opp = basis * hoogte
    print("De oppervlakte van een rechthoek met basis ", basis, "en hoogte ", hoogte, "is gelijk aan ", opp)


def omtrek_rechthoek(basis, hoogte):
    omtr = ((basis + hoogte) * 2)
    print("De omtrek van een rechthoek met basis ", basis, "en hoogte ", hoogte, "is gelijk aan ", omtr)


def opp_cirkel(straal):
    opp = math.pi * straal ** 2
    print("De oppervlakte van een cirkel met straal ", straal, "is gelijk aan ", opp)


def omtrek_cirkel(straal):
    omtr = math.pi * (straal + straal)
    print("De omtrek van een cirkel met straal ", straal, "is gelijk aan ", omtr)


def graden_in_hoek(hoeken):
    graden = (hoeken - 2) * 180
    print("Er zit ", graden, "graden in een ", hoeken, "-hoek")
