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


Dictionary_Landen = {'België' : {"Hoofdstad" : "Brussel", "Inwoners" : "11.7 miljoen", "Taal" : "NL"},
                     'Duitsland' : {"Hoofdstad" : "Berlijn", "Inwoners" : "80.1 miljoen", "Taal" : "Duits"},
                     'Frankrijk' : {"Hoofdstad" : "Parijs", "Inwoners" : "67.8 miljoen", "Taal" : "Frans"}}
