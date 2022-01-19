personen = int(input("Hoeveel personen? "))
totaleKost = 0
persoonKost = 0

for i in range(0, personen):
    print("Hou oud is persoon", i+1)
    age = int(input())
    if age < 12:
        persoonKost = 4
    elif age < 18:
        persoonKost = 5
    elif age > 18:
        persoonKost = 6

    student = input("Heeft u een studenten kaart? ja of nee? ")
    if student == "ja" and age < 26:
        persoonKost = persoonKost - 2

    langSpeel = input("is het een langspeel film? ja of nee? ")
    if langSpeel == "ja":
        persoonKost = persoonKost + 2

    drieD = input("is het een 3D film? ja of nee? ")
    if drieD == "ja":
        persoonKost = persoonKost + 2

    personeel = input("is de persoon personeel of familie van personeel?")
    if personeel == "ja":
        persoonKost = persoonKost * 0.9

    totaleKost = totaleKost + persoonKost
    print("Ticket prijs voor persoon", i+1, " is gelijk aan", persoonKost, "euro")

print("Totale prijs is gelijk aan", totaleKost, "euro")
