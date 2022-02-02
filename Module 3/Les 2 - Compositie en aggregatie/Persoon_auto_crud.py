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

    def set_nieuwe_naam(self):
        nieuwe_naam = input("geef een naam")
        self.naam = nieuwe_naam

    def toon_persoons_info(self):
        return "De persoon heet {} en is {} jaar oud".format(self.naam,self.leeftijd)


class Auto:
    def __init__(self,merk,model,bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar

    def toon_auto_info(self):
        return("De auto is een {} {} van het bouwjaar {}".format(self.merk,self.model,self.bouwjaar))

#data
p = Persoon("Jan",22)

def toon_menu():
    print("Welke handeling wil je uitvoeren")
    print("1: Toon persoonsinfo")
    print("2: Verander de naam van de persoon")
    print("3: Print de wagens van de persoon")
    print("4: voeg een wagen toe")




def voeg_wagen_toe():
    merk = input("geef het merk van de wagen")
    model = input("geef het model van de wagen")
    bouwjaar = input("geef het bouwjaar van de wagen in")
    wagen = Auto(merk,model,bouwjaar)
    p.voeg_auto_toe(wagen)

# hoofdprogramma
toon_menu()
keuze = input("geef je keuze in:")
while(not keuze == "stop"):
    if(keuze == "1"):
         print(p.toon_persoons_info())
    elif(keuze == "2"):
        p.set_nieuwe_naam()
    elif(keuze == "3"):
        p.print_wagens()
    elif(keuze == "4"):
        voeg_wagen_toe()
    keuze = input("geef je keuze in:")

