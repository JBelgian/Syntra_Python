from datetime import date

date1 = date(2021, 10, 11)
date2 = date(2021, 12, 25)

delta = date2 - date1

print(delta.days)
