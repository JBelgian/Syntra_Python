# Oefening autoverhuur
"""""
- Schrijf een programma voor een autoverhuur firma. 
- Data wordt bijgehouden in een dictionary{id:id_auto,merk:auto_merk,brandstof: brandstof_auto, verhuurd: verhuurd_ja/nee}
- Functies
    - toonwagens(toont alle wagen)
    - toon_beschikbare_wagens(toont wagens waar verhuurd nee is)
    - Toon_verhuurde_wagens(toont de wagen waar verhuurd ja is)
    - Verhuur_wagen(wagen id) enkel wagen die beschikbaar zijn, indien niet beschikbaar melding, deze wagen is reeds 
      verhuurd, zorg er ook voor dat de wagen hierna niet meer verhuurd kan worden.
    - Wagen_terug_beschikbaar(wagen id) de verhuurde wagen wordt terug beschikbaar gezet, melding indien wagen reeds
      beschikbaar is
"""""

# dictionary van auto's
autos = {"1-RTE-813": {"Merk": "BMW", "Brandstof": "Diesel", "Verhuurd": "ja"},
         "1-YHZ-202": {"Merk": "Mercedes", "Brandstof": "Benzine", "Verhuurd": "nee"},
         "2-ABC-345": {"Merk": "Fiat", "Brandstof": "Diesel", "Verhuurd": "nee"},
         "1-XXX-001": {"Merk": "Renault", "Brandstof": "Diesel", "Verhuurd": "ja"}
         }


# functie om alle wagens te laten zien met kenmerken
def toon_alles(lijst):
    for key, value in lijst.items():
        print("Auto", " : ", key)
        for x, y in value.items():
            print(x + " : ", value[x])
        print("\n")


# functie die de wagens laat zien die verhuurd zijn (verhuurd = 'ja')
def auto_verhuurd(lijst):
    for key, value in lijst.items():
        for k, v in value.items():
            res = v
            if res == "ja":
                print(f'{key} is verhuurd')


# functie die wagens laat zien die beschikbaar zijn voor verhuur, maar indien niet beschikbaar dit meldt. Als auto
# gekozen wordt, wordt auto niet meer beschikbaar
def kies_auto(lijst):
    print("Auto's besckikbaar voor verhuur?")
    # we tonen hier de auto's die beschikbaar zijn voor verhuur
    for key, value in lijst.items():
        for k, v in value.items():
            res = v
            if res == "nee":
                print(f'Auto met als ID {key} is beschikbaar voor verhuur')
    # we vragen hier welke auto er gekozen is voor verhuur
    keuze = input("Welke auto verkiest u? Geef de ID van de wagen in: ")
    # we passen de waarde verhuurd 'neen' in 'ja'
    lijst[keuze]['Verhuurd'] = 'ja'
    print(f'Auto met als ID {keuze} is gewijzigd naar "verhuurd."')
    toon_alles(lijst)


def auto_terug_beschikbaar(lijst):
    # We doen een print van de auto's die niet bescikbaar zijn.
    print("Volgende auto's zijn verhuurd:")
    for key, value in lijst.items():
        for k, v in value.items():
            res = v
            if res == "ja":
                print(f'{key}')
    # We vragen welke auto terug op "niet verhuurd" moet worden gezet
    keuze = input("Welke auto is terug beschikbaar? Geef ID van auto in: ")
    lijst[keuze]['Verhuurd'] = 'nee'
    print(f'Auto met als ID {keuze} is gewijzigd naar "niet verhuurd."')
    toon_alles(lijst)


def menu():
    print("1. Toon alle auto's:")
    print("2. Toon alle auto's die reeds verhuurd zijn")
    print("3. Toon auto's die beschikbaar zijn voor verhuur en kies de auto die je wilt huren.")
    print("4. Toon de wagens die terug beschikbaar zijn voor verhuur.")
    print("--------------------------------------------------------------------------------------")


while True:
    menu()
    keuze = input("Geef uw keuze in: ")
    if keuze == "1":
        toon_alles(autos)
    elif keuze == "2":
        auto_verhuurd(autos)
    elif keuze == "3":
        kies_auto(autos)
    elif keuze == "4":
        auto_terug_beschikbaar(autos)
