name = input('Type your name: ')
age = ''
repetitions = ''
year = 2019

while age != int and repetitions != int:
    try:
        age = int(input('Type your age: '))
        repetitions = int(input('Type desired number of repetitions: '))
        break
    except ValueError:
        print('input must be a number, try again!')


print(f'{name}, you will turn 100 in year {(year-age)+100} \n' * repetitions)

'''
Works aswell
for i in range(repetitions):
    print(f'{name}, you will turn 100 in year {(year-age)+100}')
'''