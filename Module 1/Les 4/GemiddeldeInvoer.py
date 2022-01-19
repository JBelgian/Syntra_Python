aantal = 0
som = 0
invoer = ""

while not invoer == "stop":
    invoer = input("Geef een getal in ")
    if invoer == "stop":
        break
    else:
        try:
            invoer = int(invoer)
            som = som + invoer
            aantal = aantal + 1
        except ValueError:
            print("Gelieve een geheel getal in te geven")

print("Het gemiddelde is", som / aantal)
