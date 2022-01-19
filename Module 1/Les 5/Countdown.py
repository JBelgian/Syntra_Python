import time

vraag = "Wat is de hoofdstad van Belgie? " \
         "A - Brussel" \
         "B - Amsterdam" \
         "C - Turijn"
print(vraag)
counter = 15
score = 0
try:
    while counter > 0:
        print(counter)
        counter -= 1
        time.sleep(1)
except KeyboardInterrupt:
    answer = input("Geef antwoord in")
    if answer == "a":
        score = score + counter
    else:
        score = score
print(score)
