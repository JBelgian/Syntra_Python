class Dier():
    def __init__(self,naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
    def toon_info_dier(self):
        print("ik ben een dier met naam {} en ik ben {} jaar oud ".format(self.naam,self.leeftijd))

class Hond(Dier):
    def __init__(self,naam,leeftijd,ras):
        super().__init__(naam,leeftijd)
        self.ras = ras

    def toon_hond_info(self):
        print("Ik ben een hond met naam {} met leeftijd {} en ras {}".format(self.naam,self.leeftijd,self.ras))


d = Dier("Teddy",30)
h = Hond("Tobby",30,"Poedel")

d.toon_info_dier()
h.toon_info_dier()
h.toon_hond_info()
h.
