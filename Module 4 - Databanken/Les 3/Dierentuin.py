class Voedsel:

    def __init__(self,idVoedsel,naam,kostprijs):
        self.idVoedsel = idVoedsel
        self.naam = naam
        self.kostprijs = kostprijs

    def __str__(self):
        return "id: {} naam {} kostprijs {}".format(self.idVoedsel,self.naam,self.kostprijs)

class Dier:

    def __init__(self,idDier,naam,soort,geslacht):
        self.idDier = idDier
        self.naam = naam
        self.soort = soort
        self.geslacht = geslacht

    def voedsel(self,voedsel):
        self.voedsel = voedsel

    def __str__(self):
        return "Dier ID: {} naam {} \nSoort {} Geslacht {}".format(self.idDier,self.naam,self.soort,self.geslacht)

class Verzorger:
    def __init__(self,idVerzorger,naam):
        self.idVerzorger = idVerzorger
        self.naam = naam
        self.lijstdieren = []
    def voeg_dier_toe(self,dier):
        self.lijstdieren.append(dier)
    def __str__(self):
        return "ID : {} Naam {} en is verantwoordelijk voor {} dier(en)".format(self.idVerzorger,
                self.naam,len(self.lijstdieren))

    def toon_dieren(self):
        for x in self.lijstdieren:
            print(x)

#Voeg een dier toe
def voeg_dier_toe(lijst):
    id_dier = input("Geef het id van het dier")
    naam_dier = input("Geef de naam van het dier")
    soort_dier = input("Geef de diersoort in")
    geslacht_dier = input("Geef het geslacht in")
    d = Dier(id_dier,naam_dier,soort_dier,geslacht_dier)
    lijst.append(d)

def voeg_verzorger_toe():
    id_verzorger = input("Geef het id van de verzorger")
    naam_verzorger = input("Geef de naam van verzorger")
    v = Verzorger(id_verzorger,naam_verzorger)
    lijstverzorger.append(v)

def voeg_dier_toe_aan_verzorger():
    print("We gaan een dier toevoegen aan een verzorger")
    #verzorger
    print("verzorgers")
    for x in lijstverzorger:
        print(x.idVerzorger)
    #dier
    print("dier")
    for y in lijstdieren:
        print(y.idDier+" "+y.naam)
    dier_id = input("geef het id van het dier")
    for z in lijstdieren:
        if dier_id == z.idDier:
            d = Dier(z.idDier,z.naam,z.soort,z.geslacht)
    verzorger_id = input("geef het id van de verzorger")
    for a in lijstverzorger:
        if verzorger_id == a.idVerzorger:
            a.voeg_dier_toe(d)

def verwijder_dier():
    id_dier = input("geef het id van het dier")
    for x,o in enumerate(lijstdieren):
        if o.idDier == id_dier:
            lijstdieren.pop(x)


graan =  Voedsel("V1","graan",5)
hondenvoer = Voedsel("V2","Hondenbrokken",10)
d1 = Dier("d1","Blacky","Hond","V")
d2 = Dier("d2","Toby","Hond","M")
d3 = Dier("d3","Garfield","Kat","M")

lijstdieren = [d1,d2,d3]


v1 = Verzorger("v1","Jan")
v1.voeg_dier_toe(d1)
v1.voeg_dier_toe(d2)
print(v1)
v1.toon_dieren()
lijstverzorger = [v1]

#voeg_dier_toe_aan_verzorger()
#v1.toon_dieren()
verwijder_dier()
v1.toon_dieren()