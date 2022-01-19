import math

age = int(input("Geef leeftijd in "))

if age < 6:
    inkom = "gratis"
elif age < 12:
    inkom = "Inkom is 2 euro"
elif age < 18:
    inkom = "Inkom is 3 euro"
else:
    inkom = "4 euro"

print("Inkom voor een", age,"-jarige, is",inkom)