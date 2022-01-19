lijstEven = []
lijstOneven = []
even = 0
oneven = 0

for i in range(1, 11):
    getal = int(input())

    if getal % 2 == 0:
        lijstEven.append(getal)
        even = even + 1
    else:
        lijstOneven.append(getal)
        oneven = oneven + 1

print(lijstEven)
print(even)

print(lijstOneven)
print(oneven)
