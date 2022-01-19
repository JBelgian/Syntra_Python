programmeurs_dict = {
    'Jan': ['Python', 'Java', 'C#'],
    'Koen': ['C', 'Javascript', 'C#'],
    'Peter': ['Python', 'Javascript', 'PHP', 'Java'],
    'Mark': ['C++', 'Python', 'C#', 'Perl'],
}


def toon_programmeurs():
    for key, value in programmeurs_dict.items():
        talen_str = ''
        for taal in value:
            talen_str += f'{taal}, '

        # komma en spatie achter laatste taal verwijderen
        talen_str = talen_str[:-2]

        print(f'Naam: {key}, Programmeertalen: {talen_str}')


def toon_programmeurs_taal():
    taal_keuze = input('Op welke programmeertaal wil je filteren? ').lower()
    programmeurs_list = []

    for key, value in programmeurs_dict.items():
        # list van talen omzetten in lowercase
        if taal_keuze in [x.lower() for x in value]:
            programmeurs_list.append(key)

    if programmeurs_list:
        print(f'Programmeurs die {taal_keuze} kennen: ')
        for programmeur in programmeurs_list:
            print(programmeur)
    else:
        print(f'Geen enkele programmeur kent {taal_keuze}')


def verwijder_programmeur():
    print('Welke programmeur wil je verwijderen?')
    for programmeur in programmeurs_dict.keys():
        print(programmeur)
    keuze_pr = input('Keuze: ').capitalize()
    if keuze_pr in programmeurs_dict.keys():
        programmeurs_dict.pop(keuze_pr)
    else:
        print('Deze programmeur bestaat niet')


def voeg_taal_toe():
    print('Aan Welke programmeur wil je een programmeertaal toevoegen?')
    for programmeur in programmeurs_dict.keys():
        print(programmeur)

    keuze_pr = input('Keuze: ').capitalize()
    if keuze_pr in programmeurs_dict.keys():
        keuze_taal = input('Welke taal wil je toevoegen: ').capitalize()
        if keuze_taal not in [x.capitalize() for x in programmeurs_dict[keuze_pr]]:
            programmeurs_dict[keuze_pr].append(keuze_taal)
        else:
            print(f'{keuze_pr} kent deze taal al')
    else:
        print('Deze programmeur bestaat niet')


def voeg_programmeur_toe():
    nieuwe_pr = input('Naam van nieuwe programmeur: ').capitalize()

    if not nieuwe_pr.isalpha():
        print('Naam mag enkel uit letters bestaan')
    else:
        programmeurs_dict.update({nieuwe_pr: []})
