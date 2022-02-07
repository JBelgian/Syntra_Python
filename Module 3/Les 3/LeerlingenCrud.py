class Persoon:
    def __init__(self, naam, leeftijd, woonplaats):
        self.naam = naam
        self.leeftijd = leeftijd
        self.woonplaats = woonplaats

    def toon_persoons_info(self):
        return "De persoon heet {} en is {} jaar oud en woont in {}".format(self.naam, self.leeftijd,
                                                                            self.woonplaats)


class Leerkracht(Persoon):
    def __init__(self, naam, leeftijd, woonplaats, vakken):
        super().__init__(naam, leeftijd, woonplaats)
        self.vakken = vakken

    def toon_leerkracht_info(self):
        return self.toon_persoons_info()

    def toon_vakken(self):
        vakken_string = ""
        if isinstance(self.vakken, list):
            for x in self.vakken:
                vakken_string += x + "\n"
        else:
            vakken_string += self.vakken
        return vakken_string


class Leerling(Persoon):
    def __init__(self, naam, leeftijd, woonplaats, studierichting):
        super().__init__(naam, leeftijd, woonplaats)
        self.studierichting = studierichting

    def toon_leerling_info(self):
        return "{} en volgt de studierichting {}".format(self.toon_persoons_info(), self.studierichting)


# data
llg1 = Leerling("Bjorn", 30, "Bilzen", "TEW")
llg2 = Leerling("Inge", 42, "Hasselt", "Tolk")
llg3 = Leerling("Martine", 48, "Hasselt", "Geschiedenis")
llg4 = Leerling("Peter", 35, "Bilzen", "ICT")
llg5 = Leerling("Sara", 26, "Hasselt", "Psychologie")
llg6 = Leerling("Johan", 33, "Genk", "LO")

# lijst Leerlingen
leerlingen = [llg1, llg2, llg3, llg4, llg5, llg6]


# functies
def toon_menu():
    print("1: toon alle leerlingen")
    print("2: wijzig studierichting van een leerling")
    print("3: wijzig woonplaats van de leerlingen")
    print("4: voeg een leerling toe")
    print("5: verwijder een leerling")
    print("6: sorteer leerlingen op naam")
    print("7: zoek leerling per woonplaats")


# 1: toon alle leerlingen
def toon_alle_leerlingen(lijst):
    for x in lijst:
        print(x.toon_leerling_info())


# 2: wijzig studierichting van een leerling
def wijzig_studierichting(lijst):
    lln = input("van welke leerling wil je de studierichting wijzigen ")
    for x in lijst:
        if x.naam == lln:
            studierichting = input("geef de nieuwe studierichting in ")
            x.studierichting = studierichting


# 3: wijzig woonplaats van de leerlingen
def wijzig_woonplaats(lijst):
    lln = input("van welke leerling wil je de woonplaats wijzigen ")
    for x in lijst:
        if x.naam == lln:
            woonplaats = input("geef de naam van de woonplaats ")
            x.woonplaats = woonplaats


# 4: voeg een leerling toe
def voeg_leerling_toe(lijst):
    naam = input("Geef naam van de leerling ")
    leeftijd = input("Geef de leeftijd van de leerling ")
    woonplaats = input("Geef de woonplaats van de leerling ")
    richting = input("Geef de studierichting van de leerling in ")
    llg = Leerling(naam, leeftijd, woonplaats, richting)
    lijst.append(llg)


# 5: verwijder een leerling
def verwijder_leerling(lijst):
    lln = input("geef de naam in vak de leerling")
    for x, o in enumerate(lijst):
        if o.naam == lln:
            lijst.pop(x)
            print("Leerling", lln, "is verwijderd")
        else:
            print("Leerling bestaat niet")


# 6: sorteer leerlingen op naam
def sorteer_leerlingen(lijst):
    lijst.sort(key=lambda x: x.naam)
    for x in lijst:
        print(x.toon_leerling_info())


# 7: zoek leerling per woonplaats
def toon_leerling_op_woonplaats(lijst):
    woonplaats = input("Geef de naam van de woonplaats ")
    for x in lijst:
        if x.woonplaats == woonplaats:
            print(x.toon_leerling_info())


# hoofdprogramma
toon_menu()
keuze = input("geef een keuze in ")
while not keuze == "stop":
    if keuze == "1":
        toon_alle_leerlingen(leerlingen)
    elif keuze == "2":
        wijzig_studierichting(leerlingen)
    elif keuze == "3":
        wijzig_woonplaats(leerlingen)
    elif keuze == "4":
        voeg_leerling_toe(leerlingen)
    elif keuze == "5":
        verwijder_leerling(leerlingen)
    elif keuze == "6":
        sorteer_leerlingen(leerlingen)
    elif keuze == "7":
        toon_leerling_op_woonplaats(leerlingen)
    keuze = input("geef je keuze in ")
