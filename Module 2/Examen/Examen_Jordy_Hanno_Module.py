vertalers_Limburg = {
    "Jan Peters": {"Moedertaal": "Nederlands", "Talen": ["Frans", "Duits", "Spaans", "Nederlands"],
                   "Beschikbaar": "nee"},
    "Claudio Da Franco": {"Moedertaal": "Italiaans", "Talen": ["Nederlands", "Frans", "Italiaans"],
                          "Beschikbaar": "ja"},
    "Nadia Hermandez": {"Moedertaal": "Nederlands", "Talen": ["Nederlands", "Spaans", "Engels"], "Beschikbaar": "ja"},
    "Carlos Hermandez": {"Moedertaal": "Spaans", "Talen": ["Spaans", "Engels", "Portugees", "Nederlands"],
                         "Beschikbaar": "ja"},
    "Jean-Marie Du jardin": {"Moedertaal": "Frans", "Talen": ["Frans", "Italiaans", "Nederlands"], "Beschikbaar": "ja"},
    "Fatima El Hamza": {"Moedertaal": "Nederlands", "Talen": ["Arabisch", "Nederlands", "Frans", "Engels"],
                        "Beschikbaar": "ja"}
}

vertalers_Antwerpen = {
    "Bertha Heinz": {"Moedertaal": "Nederlands", "Talen": ["Duits", "Italiaans", "Nederlands", "Nederlands"],
                     "Beschikbaar": "ja"},
    "Olga Jansen": {"Moedertaal": "Nederlands", "Talen": ["Pools", "Russisch", "Nederlands"], "Beschikbaar": "ja"},
    "Peter Jansen": {"Moedertaal": "Nederlands", "Talen": ["Duits", "Russisch", "Nederlands", "Engels"],
                     "Beschikbaar": "nee"},
    "Julia Gonzales": {"Moedertaal": "Nederlands", "Talen": ["Spaans", "Engels", "Nederlands"],
                       "Beschikbaar": "nee"},
    "Roberto Di Carlo": {"Moedertaal": "Nederlands", "Talen": ["Italiaans", "Frans", "Nederlands"],
                         "Beschikbaar": "ja"},
    "Brigitte Dewinter": {"Moedertaal": "Nederlands", "Talen": ["Zweeds", "Noors", "Nederlands"],
                          "Beschikbaar": "ja"},
    "Mohammed El Hamza": {"Moedertaal": "Nederlands", "Talen": ["Arabisch", "Nederlands", "Engels"],
                          "Beschikbaar": "nee"},
    "Yusef El Hamza": {"Moedertaal": "Nederlands", "Talen": ["Arabisch", "Nederlands", "Frans"],
                       "Beschikbaar": "ja"}
}


# Menu opties
def menu():
    print("Opties")
    print("0: Provincie veranderen")
    print("1: Toon alle vertalers")
    print("2: Toon beschikbare vertalers")
    print("3: Voeg een nieuwe vertaler toe")
    print("4: Verwijder een vertaler")
    print("5: Voeg een nieuwe taal toe")


# Toon alle vertalers
def toon_alle(lijst):
    for key, value in lijst.items():
        print("Naam vertaler", " : ", key)
        for x, y in value.items():
            print(x + " : ", value[x])
        print("\n")


# functie alle beschikbare vertalers toont (beschikbaar = 'ja')
def beschikbare_vertalers(lijst):
    for key, value in lijst.items():
        for k, v in value.items():
            res = v
            if res == "ja":
                print(f'{key} is beschikbaar')


# voeg een nieuwe vertaler toe
def voeg_vertaler(lijst):
    naam = input("Geef de voor en achternaam van de vertaler in: ")
    moedertaal = input("Wat is de vertaler zijn/haar moedertaal: ")
    beschikbaar = input("Is vertaler beschikbaar of niet? (ja/nee): ")
    gekende_talen = []
    aantal_talen = int(input("Hoeveel talen kent de vertaler? "))
    for i in range(aantal_talen):
        talen = input("Welke taal kent de vertaler: ")
        gekende_talen.append(talen)
    ww = ""
    ww_vraag = input("Om te bevestigen, typ wachtwoord in ")
    while not ww_vraag == ww:
        print("wachtwoord niet correct, probeer opnieuw")
        ww_vraag = input("Om te bevestigen, typ wachtwoord in ")
        if ww_vraag == "geef op":
            break
    if ww_vraag == ww:
        lijst.update({naam: {"Moedertaal": moedertaal, "Talen": gekende_talen, "Beschikbaar": beschikbaar}})
        print(naam, "werd toegevoegd aan de lijst")


# Verwijder een vertaler
def verwijder_vertaler(lijst):
    naam = input("Geef de naam van de vertaler die je wilt verwijderen: ")
    if naam in lijst:
        ww = "Verwijder"
        ww_vraag = input("Om te bevestigen, typ wachtwoord in ")
        while not ww_vraag == ww:
            print("wachtwoord niet correct, probeer opnieuw")
            ww_vraag = input("Om te bevestigen, typ wachtwoord in ")
            if ww_vraag == "geef op":
                break
        if ww_vraag == ww:
            lijst.pop(naam)
            print(naam, "is verwijderd van de lijst")
    else:
        print("Vertaler staat niet in de lijst en kan dus niet verwijderd worden.")


# Taal toevoegen
def voeg_taal_toe(lijst):
    naam = input("Geef de naam van de vertaler waarvan je de talen wilt aanpassen: ")
    if naam in lijst:
        naam_update = naam
        mt_update = lijst[naam].get("Moedertaal")
        beschikbaar_update = lijst[naam].get("Beschikbaar")
        talen_lijst = lijst[naam].get("Talen")
        toevoeging = input("Welke taal wil je toevoegen: ")
        while not toevoeging.isalpha():
            print("Toegevoegde taal heeft onbekende karakter probeer opnieuw")
            toevoeging = input("Welke taal wil je toevoegen: ")
        if toevoeging.isalpha():
            talen_lijst.append(toevoeging)
            lijst.pop(naam)
            lijst.update({naam_update: {"Moedertaal": mt_update, "Talen": talen_lijst, "Beschikbaar": beschikbaar_update}})

    else:
        print("Vertaler staat niet in de lijst en kan dus niet aangepast worden.")


def kies_vertaler(lijst):
    print("vertaler beschikbaar?")
    # we tonen hier de vertalers die beschikbaar
    beschikbare_vertalers(lijst)
    # we vragen hier welke auto er gekozen is voor verhuur
    keuze = input("Welke vertaler verkiest u? ")
    # we passen de waarde verhuurd 'neen' in 'ja'
    lijst[keuze]['Beschikbaar'] = 'nee'
    print(f'{keuze} is gewijzigd naar niet beschikbaar')
    toon_alle(lijst)


def lijst_vertaler_regio():
    for key, value in vertalers_Limburg.items():
        print(key, "- Regio:", "Limburg")
    for key, value in vertalers_Antwerpen.items():
        print(key, "- Regio:", "Antwerpen")
