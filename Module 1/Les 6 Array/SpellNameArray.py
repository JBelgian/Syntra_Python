naam = input("Geef naam in ")
naamLijst = []

for i in range(0, len(naam)):
    letter = naam[i:i+1]
    naamLijst.append(letter)

print(naamLijst)
