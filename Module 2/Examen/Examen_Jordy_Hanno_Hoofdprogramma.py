import Examen_Jordy_Hanno_Module

VM = Examen_Jordy_Hanno_Module

while True:
    provincie_keuze = input("Welke provincie zoekt u? 1 - Limburg, 2 - Antwerpen,  3 - Toon alle vertaler en regio of "
                            "'stop' om te stoppen ")
    if provincie_keuze == "1":
        VM.menu()
        menu_keuze = input("Uw keuze: ")
        if menu_keuze == "1":
            VM.toon_alle(VM.vertalers_Limburg)
        elif menu_keuze == "2":
            VM.beschikbare_vertalers(VM.vertalers_Limburg)
        elif menu_keuze == "3":
            VM.voeg_vertaler(VM.vertalers_Limburg)
        elif menu_keuze == "4":
            VM.verwijder_vertaler(VM.vertalers_Limburg)
        elif menu_keuze == "5":
            VM.voeg_taal_toe(VM.vertalers_Limburg)
        elif menu_keuze == "6":
            VM.kies_vertaler(VM.vertalers_Limburg)
        else:
            continue
    elif provincie_keuze == "2":
        VM.menu()
        menu_keuze = input("Uw keuze: ")
        if menu_keuze == "1":
            VM.toon_alle(VM.vertalers_Antwerpen)
        elif menu_keuze == "2":
            VM.beschikbare_vertalers(VM.vertalers_Antwerpen)
        elif menu_keuze == "3":
            VM.voeg_vertaler(VM.vertalers_Antwerpen)
        elif menu_keuze == "4":
            VM.verwijder_vertaler(VM.vertalers_Antwerpen)
        elif menu_keuze == "5":
            VM.voeg_taal_toe(VM.vertalers_Antwerpen)
        elif menu_keuze == "6":
            VM.kies_vertaler(VM.vertalers_Antwerpen)
        else:
            continue
    elif provincie_keuze == "3":
        VM.lijst_vertaler_regio()
    elif provincie_keuze == "stop":
        break
