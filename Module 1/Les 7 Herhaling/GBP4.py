gbp = float(input("Geef GBP in "))
keuze = input("1-euro; 2-dollar; 3-yen, 4-BTC ")

if keuze == "1":
    euro = gbp * 1.18
    print(euro)
elif keuze == "2":
    dollar = gbp * 1.38
    print(dollar)
elif keuze == "3":
    yen = gbp * 156.53
    print(yen)
else:
    btc = gbp * 0.000029
    print(btc)
