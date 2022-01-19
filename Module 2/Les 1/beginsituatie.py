""""
In dit programma passen we diverse functies toe op een lijst.
De gebruiker geeft een invoer welke functie hij wil aanroepen
indien de gebruiker stop invoert stop het programma
"""
#deze functie drukt de mogelijkheden af
def print_mogelijke_functies():
    print("je kan kiezen uit")
    print("1: Toon lijst om de lijst te tonen")
    print("2: voeg toe om een naam toe te voegen")
    print("3: zoek naam in de lijst")
    print("4: verwijder naam uit de lijst")
    print("5: sorteer de lijst van A-Z")
    print("6: vervang naam in lijst")

#deze functie geeft de lijst van de namen
def print_lijst(lijst):

    print("de namen in de lijst zijn")
    for element in lijst:
        print(element)

#de functie voegt een nieuw item toe
def voeg_toe(lijst):

    meer_namen = input("wil je meer dan 1 naam ingeven j/n")
    naam = ""
    if(meer_namen == "j"):
        naam = input("geef de naam van de persoon")
        while(not naam == "einde"):
            if not naam in lijst:
                bevestig = input("Ben je zeker dat je "+naam+" wilt toevoegen j/n?")
                if(bevestig == "j"):
                    lijst.append(naam)
            else:
                print(naam,"is reeds in lijst")
            naam = input("geef de naam van de persoon")
    else:
        naam = input("geef de naam van de persoon")
        if not naam in lijst:
            bevestig = input("Ben je zeker dat je "+naam+" wilt toevoegen j/n?")
            if(bevestig == "j"):
                lijst.append(naam)
        else:
            print(naam,"is reeds in lijst")
    return lijst


#de functie zoekt een naam in de lijst
def zoek_naam(lijst):
    naam = input("geef de gewenste naam in")
    if naam in lijst:
        print("naam is in de lijst")
    else:
        print("naam is niet in de lijst")

#verwijderd een naam uit de lijst
def verwijder_naam(lijst):
    naam = input("geef de naam die je wenst te verwijderen")
    if naam in lijst:
        bevestig = input("Ben je zeker dat je "+naam+" wilt verwijderen j/n")
        if(bevestig == "j"):
            lijst.remove(naam)
            print(naam," is weg uit de lijst")
    else:
        print(naam, "is niet in de lijst")
#Lijst van A-Z
def sorteer_lijst(lijst):
    lijst.sort()
    print("lijst is gesorteerd")

#functie verander naam
def vervang_in_naam_lijst(lijst):
    naam = input("geef de naam in")
    if naam in lijst:
        nieuwe_naam = input("geef een nieuwe naam")
        if not nieuwe_naam in lijst:
            lijst[lijst.index(naam)] = nieuwe_naam
            print(naam," is vervangen door ",nieuwe_naam)
        else:
            print(nieuwe_naam," staat al in de lijst")
    else:
        print("naam staat niet in de lijst")



#lijst met namen(hardcoded)
namen = ["Bart","Sofie","Mark","Evelien"]


#hoofdprogramma
print_mogelijke_functies()
invoer = input("Wat wil je doen? geef het nummer in of stop om te stoppen")
while(not invoer == "stop"):
    if(invoer == "1"):
        print_lijst(namen)
    elif(invoer == "2"):
        namen = voeg_toe(namen)
    elif(invoer == "3"):
        zoek_naam(namen)
    elif(invoer == "4"):
        verwijder_naam(namen)
    elif(invoer == "5"):
        sorteer_lijst(namen)
    elif(invoer == "6"):
        vervang_in_naam_lijst(namen)

    print_mogelijke_functies()
    invoer = input("Wat wil je doen? geef het nummer in of stop om te stoppen")
