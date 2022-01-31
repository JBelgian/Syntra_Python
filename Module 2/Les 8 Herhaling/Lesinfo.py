# Tupple
steden_tupple = ("Parijs", "Londen", "Rome", "Madrid")  # Ronde haakjes gebruiken

# Tupple afdrukken
print(steden_tupple)
print(steden_tupple[1])  # indexbased startend op 0
for element in steden_tupple:  # for loop voor afdruk vd tupple
    print(element)

# update van een tupple
'Gaat niet, tupples wijn onaanpasbaard dus update kan niet, enkel via omweg - tupple --> lijst'

lijst_steden = list(steden_tupple)  # tupple omzetten naar lijst
lijst_steden[2] = "Brussel"  # 3de entry wijzigen naar Brussel
steden_tupple = tuple(lijst_steden)  # lijst terug omzetten naar tupple
print(steden_tupple)

print("-------------------------------------------------------------------------------------------------------------")

# Set
valuta = {"Euro", "Pond", "Dollar", "Yen"}  # set haakjes gebruiken

# set afdrukken
print(valuta)  # set niet indexed, dus geen vaste volgorde
for x in valuta:  # for loop voor afdruk vd getallen
    print(x)

# item toevoegen in set
valuta.add("Gulden")  # .add gebruiken
print(valuta)

# item verwijderen in set
valuta.remove("Euro")  # .remove gebruiken
print(valuta)

# set naar lijst omzetten
valuta_lijst = list(valuta)
print(valuta_lijst)

print("-------------------------------------------------------------------------------------------------------------")

# Dictionary
cursist = {"Naam": "Frank", "Leeftijd": 25}  # Set haakjes gevolgd door key: value, ...

# Dictionary afdrukken
print(cursist)
print(cursist["Naam"])
print(cursist["Leeftijd"])

# bestaat de key?
print(cursist.get("Naam", "Niet gevonden"))  # Returned ofwel de key indien gevonden of 2de argument
print(cursist.get("Woonplaats", "Niet gevonden"))

# aanpassen van item
cursist["Naam"] = "Mark"
print(cursist)
# of
cursist.update({"Leeftijd": 66})  # .update gebruiken
print(cursist)

# key aanmaken
cursist["Hobby"] = "Voetbal"
print(cursist)

# key verwijderen
cursist.pop("Leeftijd")  # .pop gebruiken
print(cursist)

"""""
# Queue
import queue

q1 = queue.Queue(3)
q1.put("Ben")
q1.put("Harry")
q1.put("Simon")
print(q1.full())

# item uit queue halen
item = q1.get()  # Het element wordt verwijderd uit de queue na een get

print('Het item uit de queue is: ',item)

# alle elementen in queue printen
for i in range(q1.maxsize):
    print(q1.get())
"""""

# ASCII
# ASCII waarde van een teken vinden
print(ord('p'))  # ord() gebruiken

# ASCII waarde naar een teken omzetten
print(chr(65))  # chr() gebruiken


