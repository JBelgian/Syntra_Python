vm = float(input("Hoeveel m² moet gelegd worden? "))
soort = input("Welke soort tegel? 30x30, 40x40 of 50x50? ")

if vm < 100 and soort == "30x30":
    kost = vm * 18 + vm * 15
elif vm < 100 and soort == "40x40":
    kost = vm * 22 + vm * 15
elif vm < 100 and soort == "50x50":
    kost = vm * 25 + vm * 15
elif vm > 100 and soort == "30x30":
    kost = (vm * 18 + vm * 15) * 0.95
elif vm > 100 and soort == "40x40":
    kost = (vm * 22 + vm * 15) * 0.95
else:
    kost = (vm * 25 + vm * 15) * 0.95

print(vm, "m² van soort", soort, " en plaatsen kost", kost)