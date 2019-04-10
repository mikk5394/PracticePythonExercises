

number = int(input('Type a number: '))

if number == 4:
    print("4 is the special number")
elif number %2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')

#extras

num = int(input('Type a number: '))
check = int(input('Type a number: '))

if num %check == 0:
    print('Check divides evenly into num')
else:
    print('Check does not divide evenly into num')