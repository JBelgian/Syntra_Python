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
    def toon_persoons_info(self):
        return "De persoon heet {} en is {} jaar oud".format(self.naam,self.leeftijd)
    def wijzig_auto_gegevens(self):
        id = input("geef het id van de wagen")
        for x in self.wagens:
            if id == x.id:
                x.verander_info()
            else:
                print("ID bestaat niet")

    def verwijder_wagen_uit_lijst(self):
        id = input("geef het id van de wagen")
        for x,o in enumerate(self.wagens):
            if id == o.id:
                self.wagens.pop(x)



class Auto:
    def __init__(self,id,merk,model,bouwjaar):
        self.id = id
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar

    def toon_auto_info(self):
        return("iD {} : De auto is een {} {} van het bouwjaar {}".format(self.id,self.merk,self.model,self.bouwjaar))
    def verander_info(self):
        self.merk = input("geef het merk van de wagen")
        self.model = input("geef het model van de wagen")
        self.bouwjaar = input("geef het bouwjaar van de wagen")
#data
p = Persoon("Jan",22)

def toon_menu():
    print("Welke handeling wil je uitvoeren")
    print("1: Toon persoonsinfo")
    print("2: Verander de naam van de persoon")
    print("3: Print de wagen van de persoon")
    print("4: voeg een wagen toe")
    print("5: verander auto info")
    print("6: verwijder auto")

def toon_persoons_info():
    print(p.toon_persoons_info())
def verander_naam_persoon():
    nieuwe_naam = input("geef een nieuwe naam in")
    p.naam = nieuwe_naam
def voeg_wagen_toe():
    id = input("geef het ID in")
    merk = input("geef het merk van de wagen")
    model = input("geef het model van de wagen")
    bouwjaar = input("geef het bouwjaar van de wagen in")
    wagen = Auto(id,merk,model,bouwjaar)
    p.voeg_auto_toe(wagen)



# hoofdprogramma
toon_menu()
keuze = input("geef je keuze in:")
while(not keuze == "stop"):
    if(keuze == "1"):
        toon_persoons_info()
    elif(keuze == "2"):
        verander_naam_persoon()
    elif(keuze == "3"):
        p.print_wagens()
    elif(keuze == "4"):
        voeg_wagen_toe()
    elif(keuze == "5"):
        p.wijzig_auto_gegevens()
    elif(keuze == "6"):
        p.verwijder_wagen_uit_lijst()
    keuze = input("geef je keuze in:")

