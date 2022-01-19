import math

lengte = float(input("Geef lengte in"))
gewicht = float(input("Geef gewicht in"))

bmi = gewicht/math.pow(lengte,2)

if bmi < 18.5:
    print ("Ondergewicht")
elif 18.5 < bmi < 24.9:
    print ("Normaal gewicht")
elif 25.5 < bmi < 29.9:
    print ("Overgewicht")
else:
    print ("Obese")