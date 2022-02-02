class Persoon:
    wagens = []
    def __init__(self,naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
    def voeg_auto_toe(self,Auto):
        self.wagens.append(Auto)
    def print_wagens(self):
        if len(self.wagens) == 0:
            print("Deze persoon heeft geen wagens")
        else:
            for x in self.wagens:
                print(x.toon_auto_info())


class Auto:
    def __init__(self,merk,model,bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar

    def toon_auto_info(self):
        return("De auto is een {} {} van het bouwjaar {}".format(self.merk,self.model,self.bouwjaar))


a1 = Auto("Audi","a4",2020)
a2 = Auto("Volkswagen","Golf",2016)
p = Persoon("Jan",22)
p.print_wagens()
p.voeg_auto_toe(a1)
p.voeg_auto_toe(a2)
p.print_wagens()
