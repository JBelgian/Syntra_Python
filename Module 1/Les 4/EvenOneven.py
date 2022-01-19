invoer = ""
even = 0
oneven = 0

while not invoer == "einde":
    invoer = input("Geef een getal in ")
    if invoer == "einde":
        break
    else:
        try:
            invoer = int(invoer)
            if invoer % 2 == 0:
                even = even + 1
            else:
                oneven = oneven + 1
        except ValueError:
            print("Gelieve een geheel getal in te geven")

print("Gebruiker heeft", even, "even getallen en", oneven, "oneven getallen ingegeven")
