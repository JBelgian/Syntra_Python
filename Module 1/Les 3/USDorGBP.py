euro = float(input("Geef bedrag in EUR in"))
currency = input("Omzetten naar dollar of pond?")
if currency == "dollar":
    print (euro,"EUR is gelijk aan",round(euro*1.17,2),"USD")
elif currency == "pond":
    print (euro,"EUR is gelijk aan",round(euro*0.85,2),"GBP")
else:
    print ("Currency niet juist ingevuld")