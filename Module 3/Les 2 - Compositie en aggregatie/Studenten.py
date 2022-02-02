import Student as Stud


def toon_menu():
    print("1: toon lijst met studenten")
    print("2: verander student naam")
    print("3: verander studierichting student")
    print("4: voeg student toe")
    print("5: verwijder student")


def toon_lijst_studenten():
    print("Lijst met studenten")
    print("--------------------------")
    for x in Stud.lijst_studenten:
        print(x.toon_student_info())


def verander_student_naam():
    zoek_naam = input("geef de naam in van de gezochte student")
    for x in Stud.lijst_studenten:
        if x.naam == zoek_naam:
            nieuwe_naam = input("geef een nieuwe naam voor de student")
            x.verander_naam(nieuwe_naam)


def verander_student_richting():
    zoek_naam = input("geef de naam in van de gezochte student")
    for x in Stud.lijst_studenten:
        if x.naam == zoek_naam:
            nieuwe_richting = input("geef een nieuwe studierichting in")
            x.verander_richting(nieuwe_richting)


def voeg_student_toe():
    naam = input("geef de naam van de student")
    studierichting = input("Welke studierichting volgt de studenten")
    Stud.lijst_studenten.append(Stud.Student(naam, studierichting))


def verwijder_student():
    zoek_naam = input("geef de naam in van de gezochte student")
    for x, o in enumerate(Stud.lijst_studenten):
        if o.naam == zoek_naam:
            Stud.lijst_studenten.pop(x)


toon_menu()
keuze = input("geef je keuze in:")
while not keuze == "stop":
    if keuze == "1":
        toon_lijst_studenten()
    elif keuze == "2":
        verander_student_naam()
    elif keuze == "3":
        verander_student_richting()
    elif keuze == "4":
        voeg_student_toe()
    elif keuze == "5":
        verwijder_student()

    keuze = input("geef je keuze in:")
