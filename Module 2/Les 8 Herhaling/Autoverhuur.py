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
    - Voeg wagen toe(id,merk,model,brandstof,verhuurd=“nee”)
    - Verwijder wagen(id) melding indien id niet bestaat. 
    - Logboek(IO) 
        - Schrijf telkens naar een bestand welke acties er uitgevoerd zijn.
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
    log = open("logboek.txt", "a")
    log.writelines("Lijst auto's wordt getoond" + "\n")
    log.close()


# functie die de wagens laat zien die verhuurd zijn (verhuurd = 'ja')
def auto_verhuurd(lijst):
    for key, value in lijst.items():
        for k, v in value.items():
            res = v
            if res == "ja":
                print(f'{key} is verhuurd')
    log = open("logboek.txt", "a")
    log.writelines("Lijst verhuurde auto's wordt getoond" + "\n")
    log.close()


# functie die wagens laat zien die beschikbaar zijn voor verhuur, maar indien niet beschikbaar dit meldt.
# Als auto gekozen wordt, wordt auto niet meer beschikbaar
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
    log = open("logboek.txt", "a")
    log.writelines("Auto met ID " + keuze + " werd op verhuurd veranderd." + "\n")
    log.close()


# met die functie geven we aan de auto's die verhuurd zijn
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
    log = open("logboek.txt", "a")
    log.writelines("Auto met ID " + keuze + " werd op niet verhuurd veranderd." + "\n")
    log.close()


# voeg een wagen toe
def voeg_auto(lijst):
    id = input("Geef de ID van de auto in: ")
    merk = input("Van welke merk is de auto?: ")
    brandstof = input("Welke brandstof?: ")
    verhuurd = input("Is de auto verhuurd of niet? (ja/nee): ")
    lijst.update({id: {"Merk": merk, "Brandstof": brandstof, "Verhuurd": verhuurd}})
    log = open("logboek.txt", "a")
    log.writelines("Auto met ID " + id + " werd toegevoegd aan de lijst met auto's." + "\n")
    log.close()


# verwijderen van een auto, melding indien deze niet bestaat
def verwijder_auto(lijst):
    auto = input("Geef de ID van de auto die je wilt verwijderen: ")
    if auto in lijst:
        lijst.pop(auto)
        log = open("logboek.txt", "a")
        log.writelines("Auto met ID " + auto + " werd verwijderd uit de lijst." + "\n")
        log.close()
    else:
        print("Auto staat niet in de lijst en kan dus niet verwijderd worden.")


# logbook aanmaak en lezen
def toon_logboek():
    log = open("logboek.txt", "r")
    print("-------------------Logboek--------------" + "\n")
    print(log.read())
    log.close()


# afprinten van het menu
def menu():
    print("1. Toon alle auto's:")
    print("2. Toon alle auto's die reeds verhuurd zijn")
    print("3. Toon auto's die beschikbaar zijn voor verhuur en kies de auto die je wilt huren.")
    print("4. Toon de wagens die terug beschikbaar zijn voor verhuur.")
    print("5. Voeg een nieuwe auto in;")
    print("6. Verwijder een auto uit de lijst.")
    print("7. Toon de logboek.")
    print("--------------------------------------------------------------------------------------")


# Main programma
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
    elif keuze == "5":
        voeg_auto(autos)
    elif keuze == "6":
        verwijder_auto(autos)
    elif keuze == "7":
        toon_logboek()
    elif keuze == 'stop':
        break
