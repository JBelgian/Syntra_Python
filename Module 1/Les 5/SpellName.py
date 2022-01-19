naam = input("Geef naam in ")

for i in range(0, len(naam)):
    letter = naam[i:i+1]
    print(letter)

'''Backwards 
naam = input("Geef naam in ")

for i in range(len(naam), 0):
    letter = naam[i-1:i]
    print(letter)
'''