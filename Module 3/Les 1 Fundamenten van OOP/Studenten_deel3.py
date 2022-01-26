"""""
- Maak een klasse student(naam,leeftijd,punten)
- Maak een methode toon_student_info()
- Maak een methode veranderpunten(punt) enkel punten tussen 1 en 100.
- Maak 2 lijsten klas a en klas b.
Zorg ervoor dat een leerling aangemaakt kan worden.
Toegevoegd aan een lijst.
Toon leerlingen alle leerlingen
Voeg leerling toe aan een klas
Toon klas, of alle leerlingen
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


def opties():
    print("-----------------------------")
    print("Wat wil je doen?")
    print("1 - Lijst tonen")
    print("2 - Punten veranderen")
    print("3 - Student toevoegen")
    print("4 - Toon klas")
    print("5 - Verwijder student")
    print("6 - Verander studentnaam")
    print("einde - programma sluiten")


def veranderpunten(lijst):
    zoek_naam = input("Geef naam in voor wie punten verandert worden. ")
    for x in lijst:
        if zoek_naam == x.naam:
            change = int(input("Geef nieuwe punten in. "))
            if 0 <= change <= 100:
                x.punten = change
            else:
                print("Nieuwe punten niet tussen 0 en 100")


def nieuwe_student(lijst):
    naam = input("Geef naam nieuw persoon in ")
    leeftijd = int(input("Geef leeftijd in "))
    punten = int(input("Geef punten in "))
    lijst.append(Student(naam, leeftijd, punten))


def toon_klas():
    klas_Keuze = input("Geef klas keuze in? 1 - Klas A of 2 - Klas B")
    if klas_Keuze == "1":
        for x in klas_a:
            x.toon_student_info()
    if klas_Keuze == "2":
        for x in klas_b:
            x.toon_student_info()


def verwijder_student(lijst):
    zoek_naam = input("Welke persoon wil je verwijderen? ")
    for x, o in enumerate(all_students):
        if o.naam == zoek_naam:
            del all_students[x]
            break


def verandernaam(lijst):
    zoek_naam = input("Geef naam wilt veranderen ")
    for x in lijst:
        if zoek_naam == x.naam:
            nieuwe_naam = input("Geef nieuwe naam in ")
            x.naam = nieuwe_naam


s1 = Student("Jordy", 29, 100)
s2 = Student("Jeroen", 26, 95)
s3 = Student("Sarah", 31, 88)
s4 = Student("Ilse", 28, 99)
s5 = Student("Terry", 21, 71)
s6 = Student("Maria", 25, 12)
s7 = Student("Joel", 35, 33)
s8 = Student("Emmitt", 28, 48)

all_students = [s1, s2, s3, s4, s5, s6, s7, s8]
klas_a = [s1, s2, s3, s4]
klas_b = [s5, s6, s7, s8]

while True:
    opties()
    keuze = input("Geef keuze in. ")
    print("-----------------------------")
    if keuze == "1":
        for x in all_students:
            x.toon_student_info()
    elif keuze == "2":
        veranderpunten(all_students)
    elif keuze == "3":
        nieuwe_student(all_students)
    elif keuze == "4":
        toon_klas()
    elif keuze == "5":
        verwijder_student(all_students)
    elif keuze == "6":
        verandernaam(all_students)
    elif keuze == "einde":
        break