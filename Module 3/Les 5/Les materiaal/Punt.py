class Punt:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
         return "({0},{1})".format(self.x,self.y)
    def __add__(self, other):
        x = self.x + other.x
        y =self.y + other.y
        return Punt(x,y)

p1 = Punt(5,3)
p2 = Punt(2,5)
print(p1+p2)
