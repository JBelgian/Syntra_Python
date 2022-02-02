class verloning:
    def __init__(self,maandloon,bonus):
        self.maandloon = maandloon
        self.bonus = bonus

    def bereken_jaarloon(self):
        return (self.maandloon*12)+self.bonus

class werknemer:
    def __init__(self,naam,functie):
        self.naam = naam
        self.functie = functie

    def ken_loon_toe(self,loon,bonus):
        self.loon = verloning(loon,bonus)

    def bereken_loon(self):
        jaarloon = (self.loon.maandloon*12)+self.loon.bonus


    def toon_jaarloon(self):
        print("€ ",self.loon.bereken_jaarloon())

    def persoons_info(self):
        print(self.naam+" "+self.functie)
        self.toon_jaarloon()

loon1 = verloning(2500,500)
w1 = werknemer("Jan","Boekhouder")
w1.persoons_info()
w1.ken_loon_toe(1500,50)
w1.bereken_loon()
