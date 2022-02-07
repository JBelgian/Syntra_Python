class Persoon:
    def __init__(self,naam,leeftijd,woonplaats):
        self.naam = naam
        self.leeftijd = leeftijd
        self.woonplaats = woonplaats
    def toon_persoons_info(self):
        return "De persoon heet {} en is {} jaar oud en woont in {}".format(self.naam,self.leeftijd,
                                                                            self.woonplaats)

class Leerling(Persoon):
    def __init__(self,naam,leeftijd,woonplaats,studierichting):
        super().__init__(naam,leeftijd,woonplaats)
        self.studierichting = studierichting
    def toon_leerling_info(self):
        return "{} en volgt de studierichting {}".format(self.toon_persoons_info(),self.studierichting)



class Leerkracht(Persoon):
    def __init__(self,naam,leeftijd,woonplaats,vakken):
        super().__init__(naam,leeftijd,woonplaats)
        self.vakken = vakken

    def toon_leerkracht_info(self):
        return self.toon_persoons_info()


    def toon_vakken(self):
        vakken_string = ""
        if isinstance(self.vakken,list):
            for x in self.vakken:
                vakken_string += x+"\n"
        else:
            vakken_string += self.vakken
        return vakken_string

#data
lkr1 = Leerkracht("Bjorn",30,"Bilzen",["ICT","Economie"])
lkr2 = Leerkracht("Inge",42,"Hasselt",["Nederlands","Frans","Engels"])
lkr3 = Leerkracht("Martine",48,"Hasselt",["Geschiedenis","Biologie"])
lkr4 = Leerkracht("Peter",35,"Bilzen",["ICT","Wiskunde"])
lkr5 = Leerkracht("Sara",26,"Hasselt",["Nederlands","Aardrijkskunde"])
lkr6 = Leerkracht("Johan",33,"Genk","LO")


#lijst leerkrachten
leerkrachten = [lkr1,lkr2,lkr3,lkr4,lkr5,lkr6]

#functies

def toon_menu():
    print("1: toon alle leerkrachten")
    print("2: toon vakken van een leerkracht")
    print("3: voeg Leerkracht toe")
    print("4: voeg vak toe aan een leerkracht")
    print("5: wijzig woonplaats van de leerkracht")
    print("6: toon alle leerkracht van woonplaats")
    print("7: verwijder vak")


def toon_alle_leerkrachten(lijst):
    for x in lijst:
        print(x.toon_leerkracht_info())

def toon_vakken_van_leerkracht(lijst):
    lkr = input("geef de naam van de leerkracht")
    for x in lijst:
        if x.naam == lkr:
            print(x.toon_vakken())
def voeg_leerkracht_toe(lijst):
    naam = input("Geef naam van de leerkracht")
    leeftijd = input("Geef de leeftijd van de leerkracht")
    woonplaats = input("Geef de woonplaats van de leerkracht")
    vak = input("Wil je een vak toekennen j/n")
    if(vak == "j"):
        vak = input("geef de naam van het vak")
    else:
        vak = "nog geen vak"
    lkr = Leerkracht(naam,leeftijd,woonplaats,vak)
    lijst.append(lkr)

def voeg_vak_toe_aan_leerkracht(lijst):
    lkr = input("Aan welke leerkracht wil je een vak toekennen")
    for x in lijst:
        if x.naam == lkr and len(x.vakken)<5 :
            vak = input("geef de naam van het vak")
            x.vakken.append(vak)

def wijzig_woonplaats(lijst):
    lkr = input("van welke leerkracht wil je de woonplaats wijzigen")
    for x in lijst:
        if x.naam == lkr:
            woonplaats = input("geef de naam van de woonplaats")
            x.woonplaats = woonplaats

def toon_leerkracht_op_woonplaats(lijst):
    woonplaats = input("Geef de naam van de woonplaats")
    for x in lijst:
        if x.woonplaats == woonplaats:
            print(x.toon_leerkracht_info())

def verwijder_vak_leerkracht(lijst):
    lkr = input("geef de naam in vak de leerkracht")
    for x in lijst:
        if x.naam == lkr:
            vak = input("geef de naam van het vak")
            if vak in x.vakken:
                x.vakken.remove(vak)

#hoofdprogramma
toon_menu()
keuze = input("geef een keuze in")
while(not keuze == "stop"):
    if keuze == "1":
        toon_alle_leerkrachten(leerkrachten)
    elif keuze == "2":
        toon_vakken_van_leerkracht(leerkrachten)
    elif keuze == "3":
        voeg_leerkracht_toe(leerkrachten)
    elif keuze == "4":
        voeg_vak_toe_aan_leerkracht(leerkrachten)
    elif keuze == "5":
        wijzig_woonplaats(leerkrachten)
    elif keuze == "6":
        toon_leerkracht_op_woonplaats(leerkrachten)
    elif keuze == "7":
        verwijder_vak_leerkracht(leerkrachten)
    keuze = input("geef je keuze in")
