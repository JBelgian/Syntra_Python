age = int(input("Geef leeftijd in"))
abo = input("Heeft u een abonoment? ja/nee")

if abo == "ja":
    if age < 10:
        print ("Toegang is gratis")
    elif age < 13:
        print ("Toegang is €10")
    elif age < 22:
        print ("Toegang is €15")
    else:
        print ("Toegang is €18")
elif abo == "nee":
    if age < 10:
        print ("Toegang is gratis")
    elif age < 13:
        print ("Toegang is €9")
    elif age < 22:
        print ("Toegang is €13.50")
    else:
        print ("Toegang is €16.20")  