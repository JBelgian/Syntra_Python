class Student:
    def __init__(self, naam, studierichting):
        self.naam = naam
        self.studierichting = studierichting

    def toon_student_info(self):
        return "De student heeft {} en studeert {} ".format(self.naam, self.studierichting)

    def verander_naam(self, nieuwe_naam):
        self.naam = nieuwe_naam

    def verander_richting(self, nieuwe_richting):
        self.studierichting = nieuwe_richting


stud1 = Student("Mark", "TEW")
stud2 = Student("Sofie", "Filosofie")
stud3 = Student("Inge", "Economie")
stud4 = Student("Erik", "Wiskunde")
stud5 = Student("Peter", "Informatica")

lijst_studenten = [stud1, stud2, stud3, stud4, stud5]
