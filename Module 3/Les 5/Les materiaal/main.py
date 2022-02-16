

class Rekening:
    def __init__(self,id,zichtrekening,spaarrekening):
        self.id = id
        self.zichtrekening = zichtrekening
        self.spaarrekening = spaarrekening
   def __add__(self, other):
        return self.zichtrekening + other.zichtrekening , self.spaarrekening + other.spaarrekening

r1 = Rekening("R22001",2500,10000) #12500
r2 = Rekening("R22002",3000,5000) #8000

r3 = r1 + r2


