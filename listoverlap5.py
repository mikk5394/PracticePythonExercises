import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list = []

for n in a and b:
    if n in a and b:
        list.append(n)

print(list)


#extra2

a1 = random.sample(range(1, 25), 10)
b1 = random.sample(range(1, 25), 10)

commonSet = set()

[commonSet.add(x) for x in a1 for y in b1 if x == y]

print(commonSet)