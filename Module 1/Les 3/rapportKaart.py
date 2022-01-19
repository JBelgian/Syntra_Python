Vak1 = float(input("Geef punten op vak 1 in"))
Vak2 = float(input("Geef punten op vak 2 in"))
Vak3 = float(input("Geef punten op vak 3 in"))
Vak4 = float(input("Geef punten op vak 4 in"))
Vak5 = float(input("Geef punten op vak 5 in"))

avg = (Vak1+Vak2+Vak3+Vak4+Vak5)/5

if avg < 3:
    print ("Gemiddelde is",avg,"en is zwaar onvoldoende")
elif avg < 5:
    print ("Gemiddelde is",avg,"en is onvoldoende")
elif avg < 7:
    print ("Gemiddelde is",avg,"en is voldoende")
elif avg < 8:
    print ("Gemiddelde is",avg,"en is goed")
elif avg < 10:
    print ("Gemiddelde is",avg,"en is heel goed")
elif avg == 10:
    print ("Gemiddelde is",avg,"en is prima")