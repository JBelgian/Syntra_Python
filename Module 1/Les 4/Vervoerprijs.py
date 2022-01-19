km = float(input("Geef aantal afgelegde km in "))

if km < 25:
    print(km * 0.25)
else:
    print((km-25)*0.15+25*0.25)