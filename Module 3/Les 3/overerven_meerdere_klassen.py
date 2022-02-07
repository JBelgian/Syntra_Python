class Moeder:
    def __init__(self,voornaam,naam,geboorte_jaar):
        self.voornaam = voornaam
        self.naam = naam
        self.geboorte_jaar = geboorte_jaar

    def toon_info_moeder(self):
        print("de moeder heet {} {} en is {} jaar oud".format(self.voornaam,self.naam,2022-self.geboorte_jaar))

class Vader:
    def __init__(self,voornaam,naam,geboorte_jaar):
        self.voornaam = voornaam
        self.naam = naam
        self.geboorte_jaar = geboorte_jaar

    def toon_info_vader(self):
        print("de vader heet {} {} en is {} jaar oud".format(self.voornaam,self.naam,2022-self.geboorte_jaar))

class Kind(Moeder,Vader):
    def __init__(self,vader,moeder,naam):
        self.naam = naam
        self.vader = vader
        self.moeder = moeder

    def toon_info_kind(self):
        print("het kind heet "+self.naam)
        self.moeder.toon_info_moeder()
        self.vader.toon_info_vader()


m = Moeder("Inge","Jansen",1972)
m.toon_info_moeder()
v = Vader("Bart","Claesen",1970)
v.toon_info_vader()
k = Kind(v,m,"Ben")
k.toon_info_kind()
k.moeder.voornaam = "Sofie"
k.vader.voornaam = "Karel"
k.toon_info_kind()
