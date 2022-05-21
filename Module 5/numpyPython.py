import numpy

lijst = [5, 3, 6, 7, 9, 1]
arr = numpy.array([1, 2, 3, 4, 5, 6])
print(type(lijst))
print(type(arr))

arr2 = arr.reshape(3, 2)
print(arr2)

for x in arr2:
    for y in x:
        print(y)
