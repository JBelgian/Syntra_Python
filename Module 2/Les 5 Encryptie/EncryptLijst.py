"""
Encrypt een lijst met woorden dmv caeserrotatie.
1. Zorg ervoor dat er woorden kunnen toegevoegd worden aan de lijst.
2. Zorg ervoor dat woorden verwijderd kunnen worden.
"""

def encrypt(text, s):
    result = ""

# transverse the plain text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
lijst = []
s = int(input("Geef aantal plaatsen shift in? 1-25"))
result = ""

invoer = input("Wat wil je doen? 1 - toevoegen, 2 - verwijder of stop om te stoppen")
while(not invoer == "stop"):
    if(invoer == "1"):
        meer_woorden = int(input(("Hoeveel woorden wilt u toevoegen?")))
        if not meer_woorden == "einde":
            for i in range(meer_woorden):
                woord = input("Geef woord in")
                result = encrypt(woord, s)
                lijst.append(result)
                print(lijst)
    elif(invoer == "2"):
        v_woord = input("Geef woord in om te verwijderen")
        result = encrypt(v_woord, s)
        lijst.remove(result)
        print(lijst)
