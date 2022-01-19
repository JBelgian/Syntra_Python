import math

lengte = float(input("Geef lengte in"))
gewicht = float(input("Geef gewicht in"))

bmi = gewicht/math.pow(lengte,2)

print ("Als je ", lengte," meter groot bent en ", gewicht,"kg weegt, dan is je BMI = ", bmi)