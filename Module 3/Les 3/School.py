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



class Leekracht(Persoon):
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

vakken = ["ict","wiskunde","LO"]
lkr = Leekracht("Bjorn",30,"Bilzen",vakken)
print(lkr.toon_leerkracht_info())
print(lkr.toon_vakken())
