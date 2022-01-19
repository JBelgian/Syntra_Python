import Module_Programmeurs

while True:
    print('1. Toon programmeurs')
    print('2. Toon programmeurs van bepaalde taal')
    print('3. Verwijder programmeur')
    print('4. Voeg taal toe')
    print('5. Voeg programmeur toe')
    keuze = input('Typ nummer of einde: ')
    print('')

    if keuze.lower() == 'einde':
        break

    if keuze == '1':
        Module_Programmeurs.toon_programmeurs()
    if keuze == '2':
        Module_Programmeurs.toon_programmeurs_taal()
    if keuze == '3':
        Module_Programmeurs.verwijder_programmeur()
    if keuze == '4':
        Module_Programmeurs.voeg_taal_toe()
    if keuze == '5':
        Module_Programmeurs.voeg_programmeur_toe()

    print('')
