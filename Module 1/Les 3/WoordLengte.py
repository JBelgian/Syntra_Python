woord = input("Geef een woord in")
if len(woord) < 4:
    print ("Heel kort")
elif len(woord) < 6:
    print ("Kort")
elif len(woord) < 10:
    print ("Gemiddeld")
elif len(woord) > 10:
    print ("Lang")