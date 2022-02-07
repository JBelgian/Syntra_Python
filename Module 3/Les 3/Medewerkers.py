"""
Class Medewerker:
    def __init__(self, id, naam, voornaam, startjaar):
        self.id = id
        self.naam = naam
        self.voornaam = voornaam
        self.startjaar = startjaar

    def toon_persoons_info(self):
        return "{} - De persoon heet {} {} en is gestart in {}".format(self.id, self.voornaam, self.naam,
                                                                       self.startjaar)
"""


class Bediende:
    def __init__(self, id, naam, voornaam, startjaar, basisloon):
        self.id = id
        self.naam = naam
        self.voornaam = voornaam
        self.startjaar = startjaar
        sjaar = int(startjaar)
        self.maandloon = basisloon + ((2022 - sjaar) * (basisloon * 0.02 + 10))

    def toon_bediende_info(self):
        print("{} - De persoon heet {} {} en is gestart in {}".format(self.id, self.voornaam, self.naam,
                                                                      self.startjaar))


class Arbeider:
    def __init__(self, id, naam, voornaam, startjaar, uurloon):
        self.id = id
        self.naam = naam
        self.voornaam = voornaam
        self.startjaar = startjaar
        sjaar = int(startjaar)
        self.maandloon = 40 * uurloon + ((2022 - sjaar) * 10)

    def toon_arbeider_info(self):
        print("{} - De persoon heet {} {} en is gestart in {}".format(self.id, self.voornaam, self.naam,
                                                                      self.startjaar))


a1 = Arbeider("A1", "Muss", "Kyle", 2018, 8.75)
a2 = Arbeider("A2", "Green", "Rachelle", 2016, 10.75)
a3 = Arbeider("A3", "Mann", "Mark", 1992, 11)

b1 = Bediende("B1", "Mann", "Leslie", 1995, 1800)
b2 = Bediende("B2", "Robb", "Meg", 2015, 1400)
b3 = Bediende("B3", "Tank", "Bai", 2022, 1200)

medewerkers = [a1, a2, a3, b1, b2, b3]

for x in medewerkers:
    if isinstance(x, Arbeider):
        x.toon_arbeider_info()
    else:
        x.toon_bediende_info()
print("-----------------------------")

while True:
    mwType = input("arbeider of bediende? ")
    for x in medewerkers:
        if mwType == "arbeider":
            if isinstance(x, Arbeider):
                x.toon_arbeider_info()
        else:
            if isinstance(x, Bediende):
                x.toon_bediende_info()
