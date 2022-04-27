class Boek:
    def __init__(self, id, naam, auteur):
        self.id = id
        self.naam = naam
        self.auteur = auteur

    def __str__(self):
        return "ID: {} - Titel: {} - Auteur: {} ".format(self.id, self.naam, self.auteur)

    def toon_boek_auteur(self):
        return "Titel: {} - Auteur: {}".format(self.naam, self.auteur)


class Persoon:
    def __init__(self, id, naam, geslacht):
        self.id = id
        self.naam = naam
        self.geslacht = geslacht

    def __str__(self):
        return "ID: {} - Naam: {} - Geslacht: {} ".format(self.id, self.naam, self.geslacht)


class Uitlening:
    def __init__(self, id, boek, persoon):
        self.id = id
        self.boek = boek
        self.persoon = persoon

    def __str__(self):
        return "ID {} - Boek: {} - Persoon: {}".format(self.id, self.boek.naam, self.persoon.naam)


b1 = Boek("B1", "Harry Potter", "J.K. Rowling")
b2 = Boek("B2", "Davinci Code", "Dan Brown")
b3 = Boek("B3", "LOTR", "JRR Tolkien")
b4 = Boek("B4", "GoT", "George RR Martin")

boeken = [b1, b2, b3, b4]

p1 = Persoon("P1", "Geert", "man")
p2 = Persoon("P2", "Elke", "vrouw")
p3 = Persoon("P3", "Sofie", "vrouw")
p4 = Persoon("P4", "Peter", "man")

personen = [p1, p2, p3, p4]

u1 = Uitlening("U1", b1, p3)
u2 = Uitlening("U2", b3, p2)
u3 = Uitlening("U3", b4, p1)

uitleningen = [u1, u2, u3]


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


def toon_boeken():
    for x in boeken:
        print(x)


def toon_personen():
    for x in personen:
        print(x)


def toon_uitleningen():
    for x in uitleningen:
        print(x)


def voeg_boek_toe():
    id = input("Geef het ID")
    naam = input("Geef de naam")
    auteur = input("Geef de auteur")
    b = Boek(id, naam, auteur)
    boeken.append(b)


def voeg_persoon_toe():
    id = input("Geef het ID")
    naam = input("Geef de naam")
    geslacht = input("Geef het geslacht man/vrouw/x")
    p = Persoon(id, naam, geslacht)
    personen.append(p)


def voeg_uitlening_toe():
    id = input("geef het ID")
    id_boek = input("geef het id van het boek")
    # bestaat het boek
    for x in boeken:
        if id_boek == x.id:
            b = Boek(id_boek, x.naam, x.auteur)

    id_persoon = input("geef het id van de persoon")
    for y in personen:
        if id_persoon == y.id:
            p = Persoon(id_persoon, y.naam, y.geslacht)

    if isinstance(b, Boek) and isinstance(p, Persoon):
        u = Uitlening(id, b, p)
        uitleningen.append(u)
    else:
        print("Uitlening kan niet worden toegevoegd")


def toon_uitleningen_boek():
    id_boek = input("Geef het id van het boek")
    for x in uitleningen:
        if id_boek == x.boek.id:
            print(x.persoon)
        else:
            print("Boek bestaat niet of nog niet uitgeleend")


def toon_boek_geslacht():
    geslacht = input("geef het gelacht")
    for x in uitleningen:
        if geslacht == x.persoon.geslacht:
            print(x.boek)


def sorteer_boek_AZ():
    boeken.sort(key=lambda x: x.naam)
    for x in boeken:
        print(x)


def verwijder_uitlening():
    id = input("geef het id van de uitlening")
    for x, o in enumerate(uitleningen):
        if o.id == id:
            uitleningen.pop(x)


# hoofdprogramma
while True:
    toon_menu()
    keuze = input("geef een keuze ")
    if keuze == "1":
        toon_boeken()
    elif keuze == "2":
        toon_personen()
    elif keuze == "3":
        toon_uitleningen()
    elif keuze == "4":
        voeg_boek_toe()
    elif keuze == "5":
        voeg_persoon_toe()
    elif keuze == "6":
        voeg_uitlening_toe()
    elif keuze == "7":
        toon_uitleningen_boek()
    elif keuze == "8":
        toon_boek_geslacht()
    elif keuze == "9":
        sorteer_boek_AZ()
    elif keuze == "10":
        verwijder_uitlening()
