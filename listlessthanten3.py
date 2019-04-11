a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)


#extra1

newList = []

for i in a:
    if i < 5:
        newList.append(i)

print(newList)


#extra2

newList2 = [n for n in a if n < 5]
print(newList)


#extra3

inp = int(input('At which number should the list cut? '))

newList3 = [n for n in a if n < inp]
print(newList3)
        