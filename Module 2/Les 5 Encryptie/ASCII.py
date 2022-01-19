woord = "Jordy"
lengte = len(woord)
lijst = []

#Woord naar ASCII
for i in range(lengte):
    lijst.append(ord(woord[i]))

print(lijst)

#ASCII naar woord
for j in range(lengte):
    letter = chr(lijst[j])
    print(letter)
