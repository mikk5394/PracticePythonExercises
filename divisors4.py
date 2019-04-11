

inp = int(input('Type a number: '))

myList = []

for i in range(1, inp):
    if inp%i == 0:
        myList.append(i)

print(myList)

#with list comprehension
myList2 = [i for i in range(1, inp) if inp%i == 0]

print(myList2)
