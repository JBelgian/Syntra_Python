"""""
- Maak een klasse student(naam,leeftijd,punten)
- Maak een methode toon_student_info()
- Maak een methode veranderpunten(punt) enkel punten tussen 1 en 100.
- Maak 2 lijsten klas a en klas b.
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


def veranderpuntenklas():
    klas_Keuze = input("Geef klas keuze in? 1 - klas_a of 2 - klas_b")
    if klas_Keuze == "1":
        for x in klas_a:
            print(x.naam)
        veranderpunten(klas_a)
        for x in klas_a:
            x.toon_student_info()
    elif klas_Keuze == "2":
        for x in klas_b:
            print(x.naam)
        veranderpunten(klas_b)
        for x in klas_b:
            x.toon_student_info()

def nieuwe_student():
    naam = input("Geef naam nieuw persoon in ")
    leeftijd = int(input("Geef leeftijd in "))
    punten = int(input("Geef punten in "))
    klas_Keuze = input("Geef klas keuze in? 1 - klas_a of 2 - klas_b")
    if klas_Keuze == "1":
        klas_a.append(Student(naam, leeftijd, punten))
        for x in klas_a:
            x.toon_student_info()
    elif klas_Keuze == "2":
        klas_b.append(Student(naam, leeftijd, punten))
        for x in klas_b:
            x.toon_student_info()




s1 = Student("Jordy", 29, 100)
s2 = Student("Jeroen", 26, 95)
s3 = Student("Sarah", 31, 88)
s4 = Student("Ilse", 28, 99)
s5 = Student("Terry", 21, 71)
s6 = Student("Maria", 25, 12)
s7 = Student("Joel", 35, 33)
s8 = Student("Emmitt", 28, 48)

klas_a = [s1, s2, s3, s4]
klas_b = [s5, s6, s7, s8]


nieuwe_student()
