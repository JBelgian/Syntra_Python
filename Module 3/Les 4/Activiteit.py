class Activiteit:
    def __init__(self, id, naam, kostprijs):
        self.id = id
        self.naam = naam
        self.kostprijs = kostprijs
        self.begeleider = ""

    def toon_activiteit(self):
        return "{} - Activiteitnaam: {} - Kostprijs: {}".format(self.id, self.naam, self.kostprijs)

    def voeg_begeleider_toe(self):

