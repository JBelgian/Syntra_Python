class hoofdstuk:
    def __init__(self,naam_hoofdstuk,hoofdstuk_tekst):
        self.naam_hoofdstuk = naam_hoofdstuk
        self.hoofdstuk_tekst = hoofdstuk_tekst

    def toon_hoofdstuk(self):
        return self.hoofdstuk_tekst

class boek:
    hoofdstukken = []
    def __init__(self,naam_boek):
        self.naam = naam_boek
    def voeg_hoofstuk_toe(self,hoofdstuk):
        self.hoofdstukken.append(hoofdstuk.hoofdstuk_tekst)
    def print_boek(self):
        for x in self.hoofdstukken:
            print(x)
    def voeg_lijst_hoofdstukken_toe(self,lijst):
        for x in lijst:
            self.hoofdstukken.append(x.hoofdstuk_tekst)


h1 = hoofdstuk("inleiding","Er was eens een meisje genaamd roodkapje")
h2 = hoofdstuk("midden","Oh wat heb je grote ogen ...")
h3 = hoofdstuk("Climax","De jager doodde de wolf en vulde zijn maag met stenen")
h4 = hoofdstuk("Einde","En ze leefde nog lang en gelukkig")

sprookje = boek("Rood kapje")
sprookje.voeg_hoofstuk_toe(h1)
hoofdstukken = [h2,h3,h4]
sprookje.voeg_lijst_hoofdstukken_toe(hoofdstukken)
sprookje.print_boek()

sprookje.print_boek()







