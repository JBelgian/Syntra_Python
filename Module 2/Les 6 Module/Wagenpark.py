"""
- Schrijf een applicatie waar de eigenaar zijn wagenpark kan beheren.
- Het programma is beveiligd met wachtwoord. Bonuspunten(Caeserrotatie)
    - Indien de gebruiker 3x het verkeerde wachtwoord ingeeft stopt het programma.
- Alle wagens worden opgeslagen in een dictionary in een module
    - Bevat de volgende waardes: id, merk, model, bouwjaar, brandstof
- De gebruiker kan de info opvragen, als een random auto selecteren.
- De gebruiker kan een auto toevoegen of verwijderen. Bonuspunt(indien het juiste wachtwoord)
    - Bij elke toevoeg/verwijder optie komt er een melding ben je zeker?
    - Bij het aanmaken krijgt de auto een automatisch id.
- Maak een functie Chasisnummer
    - Random gemaakt bestaat uit het volgende: BE(getal tussen 1 en 3)(3 letters)(4 getallen tussen 0 en 9)(klinker)(2 getallen tussen 2 en 5)
"""
import random
import string

klinkers = "aeuio"
chassis = str("BE")
chassis2 = random.randint(100,999)
chassis2str = str(chassis2)
chassis3 = random.choice(string.ascii_letters)
chassis4 = random.choice(string.ascii_letters)
chassis5 = random.choice(string.ascii_letters)
chassis6 = random.randint(1000,9999)
chassis6str = str(chassis6)
chassis7 = random.choice(klinkers)
full_Chassis = chassis + chassis2str + chassis3 + chassis4 + chassis5 + chassis6str + chassis7

print(full_Chassis)
