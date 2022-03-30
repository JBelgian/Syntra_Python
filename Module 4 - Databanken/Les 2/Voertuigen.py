import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="voertuigen"
)

mycursor = db.cursor()


class Voertuig:
    def __init__(self, id, merk, model, bouwjaar, brandstof, verhuurd):
        self.id = id
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.brandstof = brandstof


lijst_autos = []


def voeg_wagen_toe():
    merk = input("Geef de merk in ")
    model = input("Geef model in ")
    bouwjaar = input("Geef het bouwjaar in")
    brandstof = input("Geef brandstof type in ")
    verhuurd = input("Is de wagen verhuurd? Ja/Nee? ")
    mycursor.execute("INSERT INTO Autos(merk,model,bouwjaar,brandstof,verhuurd) VALUES (%s,%s,%s,%s,%s)",
                     (merk, model, bouwjaar, brandstof, verhuurd))
    db.commit()


def toon_wagens():
    mycursor.execute("SELECT * FROM Autos")
    for x in mycursor:
        print(*x)


def verwijder_wagen():
    toon_wagens()
    id = input("Geef het id van de wagen in die u wenst te verwijderen")
    sqlstring = "DELETE FROM Autos WHERE idAuto = " + "'" + id + "'"
    mycursor.execute(sqlstring)
    db.commit()


def toon_wagens_niet_verhuurd():
    mycursor.execute("SELECT * FROM Autos WHERE Verhuurd = 'Nee'")
    for x in mycursor:
        print(*x)


def huur_auto():
    print("Beschikbare wagens:")
    toon_wagens_niet_verhuurd()
    id = input("Geef het id van de wagen in die u wenst te huren ")
    sqlstring = "UPDATE Autos SET verhuurd = 'Ja' " + "WHERE idAuto = '" + id + "'"
    mycursor.execute(sqlstring)
    db.commit()



