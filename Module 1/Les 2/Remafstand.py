import math

kmph = float(input("Geef kmph in"))
remafstand = ((math.pow((kmph/10),2))/2)

print("Als je ",kmph, " km per uur rijdt dan is je remafstand", remafstand, "m")