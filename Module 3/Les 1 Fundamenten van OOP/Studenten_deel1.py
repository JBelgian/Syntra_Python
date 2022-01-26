"""""
- Maak een klasse student(naam,leeftijd,punten)
- Maak een methode toon_student_info()
- Maak een methode veranderpunten(punt) enkel punten tussen 1 en 100.
Maak 2 lijsten klas a en klas b.
Zorg ervoor dat een leerling aangemaakt kan worden.
Toegevoegd aan een lijst.
Toon leerlingen alle leerlingen
Voeg leerling toe aan een klas
Toon klas
Verwijder leerling
Verandernaam van leerling
"""""


class Student:
    def __init__(self, naam, leeftijd, punten):
        self.naam = naam
        self.leeftijd = leeftijd
        self.punten = punten

    def toon_student_info(self):
        print(self.naam + " " + str(self.leeftijd) + " " + str(self.punten))


def veranderpunten(lijst):
    zoek_naam = input("Geef naam in voor wie punten verandert worden. ")
    for x in lijst:
        if zoek_naam == x.naam:
            change = int(input("Geef nieuwe punten in. "))
            if 0 <= change <= 100:
                x.punten = change
            else:
                print("Nieuwe punten niet tussen 0 en 100")


s1 = Student("Jordy", 29, 100)
s2 = Student("Jeroen", 26, 95)
s3 = Student("Sarah", 31, 88)
s4 = Student("Ilse", 28, 99)

klas1 = [s1, s2, s3, s4]

veranderpunten(klas1)

for x in klas1:
    x.toon_student_info()
