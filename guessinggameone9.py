import random

number = random.randint(1,9)
counter = 0

while True:
    guess = input('Guess the random number between 1 and 9: ').lower()
    
    if guess == 'exit':
        break
    else:
        guess = int(guess)

    if guess == number:
        print('You guessed right! Guess the next number!')
        number = random.randint(1,9)
        counter += 1
        continue
    elif guess > number:
        print('Too high!')
    else:
        print('Too low!')

print(f'Games played: {counter}!')