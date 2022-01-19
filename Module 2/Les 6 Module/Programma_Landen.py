"""
- Maak een modules land_hoofdstad
- In de module zit een 2 delige dictionary. land(key) value(dict(key hoofdstad, value=de hoofdstad, key aantal_inwoners value: het aantal inwoners van het land, key=landstaal, value= de taal van het land
- Importeer deze data vanuit een andere project.
- Het programma vraagt naar een land, als het land in de lijst staat vraagt het programma, wat wil je weten.
        - Landinfo(Alles)
        - Hoofdstad
        - Aantal_inwoners
        - 1e Landstaal
- Het programma stop wanneer er eind ingetypt is, indien het land niet gekend is, is er een melding land nog niet in lijst. Zorg er ook voor dat gebruikers hoofdletters en kleine letters door elkaar kan gebruiken
"""
import Dictionary_Landen


landZoek = ""
while not landZoek == "eind":
    landZoek = input("Welk land zoekt u info over? ")
    if landZoek in Dictionary_Landen.Dictionary_Landen:
        infoKeuze = input("Wat wilt u weten? 1 - Hoofdstad, 2 - Aantal inwoners, 3 - Landstaal, 4 - alle info ")
        if infoKeuze == "1":
           print(Dictionary_Landen[landZoek]["Hoofdstad"])
        elif infoKeuze == "2":
            print(Dictionary_Landen[landZoek]["Inwoners"])
        elif infoKeuze == "3":
            print(Dictionary_Landen[landZoek]["Taal"])
        elif infoKeuze == "4":
            print(Dictionary_Landen[landZoek])
    else:
        print("Land niet gevonden in database")