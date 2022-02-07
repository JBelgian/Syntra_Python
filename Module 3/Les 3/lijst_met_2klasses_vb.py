class hond:
    def __init__(self,naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
    def print_info_hond(self):
        print("De hond heet {} en is {} jaar oud".format(self.naam,self.leeftijd))

class kat:
    def __init__(self,naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
    def print_info_kat(self):
        print("De kat heet {} en is {} jaar oud".format(self.naam,self.leeftijd))

k1 = kat("Mousti",10)
k2 = kat("Garfield",8)
h1 = hond("Toby",5)
dieren = [k1,k2,h1]

for x in dieren:
    if isinstance(x,kat):
        x.print_info_kat()
    else:
        x.print_info_hond()
print("----------------------")

dier = input("kat of hond")
for x in dieren:
    if(dier == "kat"):
        if isinstance(x,kat):
            x.print_info_kat()
    else:
        if isinstance(x,hond):
            x.print_info_hond()
