kmph = float(input("Geef gem. kmph in"))
tijd = float(input("Geef tijd (in mins) in"))

afstand = kmph * (tijd/60)

print("Als je ", kmph, " km per uur rijdt voor ", tijd, " minuten dan is je afgelegde afstand", afstand, "km")