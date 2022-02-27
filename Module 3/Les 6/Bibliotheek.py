class Boek:
    def __init__(self, id, titel, auteur):
        self.id = id
        self.titel = titel
        self.auteur = auteur

    def toon_info(self):
        return "ID: {} - Titel: {} - Auteur: {}".format(self.id, self.titel, self.auteur)

    def toon_titel(self):
        return self.titel

    def toon_auteur(self):
        return self.auteur


class Persoon:
    def __init__(self, lid_nr, naam, geslacht):
        self.lid_nr = lid_nr
        self.naam = naam
        self.geslacht = geslacht

    def toon_info(self):
        return "Lid Nr: {} - Naam: {} - Geslacht: {}".format(self.lid_nr, self.naam, self.geslacht)

    def toon_lidnr(self):
        return self.lid_nr

    def toon_naam(self):
        return self.naam

    def toon_geslacht(self):
        return self.geslacht


class Uitlening:
    def __init__(self, id, boek, persoon):
        self.id = id
        self.boek = boek
        self.persoon = persoon

    def toon_info(self):
        return "ID: {} - Boek: {} - Persoon: {}".format(self.id, self.boek.titel, self.persoon.naam)


def toon_menu():
    print("1: Toon boeken")
    print("2: Toon uitlening")
    print("3: Toon personen")
    print("4: Voeg een boek toe")
    print("5: Voeg een persoon toe")
    print("6: Nieuwe uitlening")
    print("7: Toon alle uitleningen van een boek")
    print("8: Toon boek per geslacht")
    print("9: Sorteer boeken alfabetisch op titel")
    print("10: Verwijder uitlening")


def toon_alle_boeken(lijst):
    for x in lijst:
        print(x.toon_info())


def toon_alle_personen(lijst):
    for x in lijst:
        print(x.toon_info())


def toon_alle_uitleningen(lijst):
    for x in lijst:
        print(x.toon_info())


def boek_toevoegen(lijst):
    id = input("Geef het boek ID in ")
    titel = input("Geef de titel van het boek in ")
    auteur = input("Geef de auteur van het boek in ")
    b = Boek(id, titel, auteur)
    lijst.append(b)


def persoon_toevoegen(lijst):
    lid_nr = input("Geef het lid nr in ")
    naam = input("Geef de naam van de persoon in ")
    geslacht = input("Geef het geslacht van de persoon in (M/V) ")
    p = Persoon(lid_nr, naam, geslacht)
    lijst.append(p)


def nieuwe_uitlening(lijstB, lijstP, lijstU):
    id = input("Geef het ID van de uitlening in ")
    id_p = input("Geef het ID van de persoon ")
    for x in lijstP:
        if id_p == x.toon_lidnr():
            persoon_naam = x.toon_naam()
            persoon_geslacht = x.toon_geslacht()
            p = Persoon(id_p, persoon_naam, persoon_geslacht)
    id_b = input("Geef het ID van het boek in ")
    for y in lijstB:
        if id_b == y.id:
            boek_naam = y.toon_titel()
            boek_auteur = y.toon_auteur()
            b = Boek(id_b, boek_naam, boek_auteur)
    u = Uitlening(id, b, p)
    lijstU.append(u)


def sorteer_boeken(lijst):
    lijst.sort(key=lambda x: x.titel)
    for x in lijst:
        print(x.toon_info())


b1 = Boek("B1", "Harry Potter", "J. K. Rowling")
b2 = Boek("B2", "Davinci Code", "Dan Brown")
b3 = Boek("B3", "LOTR", "JRR Tolkien")
b4 = Boek("B4", "GoT", "George RR Martin")

boeken = [b1, b2, b3, b4]

p1 = Persoon("P1", "Geert", "M")
p2 = Persoon("P2", "Elke", "V")
p3 = Persoon("P3", "Sofie", "V")
p4 = Persoon("P4", "Peter", "M")

personen = [p1, p2, p3, p4]

u1 = Uitlening("U1", b1, p3)
u2 = Uitlening("U2", b3, p2)
u3 = Uitlening("U3", b4, p1)

uitleningen = [u1, u2, u3]

# hoofdprogramma
toon_menu()
print()
keuze = input("geef je keuze in ")
while not keuze == "stop":
    if keuze == "1":
        toon_alle_boeken(boeken)
    elif keuze == "2":
        toon_alle_uitleningen(uitleningen)
    elif keuze == "3":
        toon_alle_personen(personen)
    elif keuze == "4":
        boek_toevoegen(boeken)
    elif keuze == "5":
        persoon_toevoegen(personen)
    elif keuze == "6":
        nieuwe_uitlening(boeken, personen, uitleningen)
    elif keuze == "9":
        sorteer_boeken(boeken)

    print()
    print("-----------------------------------")
    print()
    toon_menu()
    print()
    keuze = input("geef je keuze in ")
