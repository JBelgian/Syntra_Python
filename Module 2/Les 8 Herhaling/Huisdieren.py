"""""
Maak een klasse dieren: naam, soort, geslacht geluid, 
Init(naam,soort), init(naam,soort,geslacht), init (naam, soort, geslacht, geluid)
Maak een methode toon dierInfo(“naam … is een … “)
Maak een methode maak_geluid() deze maak het geluid van het dier
"""""

def toon_alles(lijst):
    for key, value in lijst.items():
        print(key, " : ", key)
        for x,y in value.items():
            print(x + " : ", value[x])
        print("\n")

def baas_dier(lijst):
    baas = input("Geef naam baas: ")
    if baas in lijst:
        print("Baas bestaat")
        soort = input("geef diersoort: ")
        if (lijst[baas]["Soort"]) == soort:
            print(f'{baas} heeft een {soort}')
        else:
            print("Dit soort heeft", baas, " niet.")
    else:
        print("Baas bestaat niet")

def soort_dier(lijst):
    soort = input("Van welk soort wil je de eigenaar(s) zien?: ")
    for key, value in lijst.items():
        for k,v in value.items():
            res = v
            if res == soort:
                print(f'{key} heeft een {soort}')

dieren = {"Arnaud":{"Naam":"Fien","Soort":"kat","Geslacht":"V"},
          "Tim":{"Naam":"Gus","Soort":"hond","Geslacht":"M"},
          "Johan":{"Naam":"Hugo","Soort":"hond","Geslacht":"M"},
          "Tom":{"Naam":"Luna","Soort":"papegaai","Geslacht":"V"}
          }
print("PRINT VAN ALLE EIGENAARS MET HUISDIEREN")
toon_alles(dieren)
print("PRINT WELKE EIGENAAR HEEFT WELKE DIERSOORT")
baas_dier(dieren)
print("PRINT EIGENAARS HEBBEN DEZELFDE DIERSOORT ")
soort_dier(dieren)