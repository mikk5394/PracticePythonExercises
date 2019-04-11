while True:

    p1 = int(input('Player 1 type 1 for paper, 2 for rock or 3 for scissors: '))
    p2 = int(input('Player 2 type 1 for paper, 2 for rock or 3 for scissors: '))
    choices = [1,2,3]

    if p1 not in choices:
        print('Input has to be either 1, 2 or 3')
        continue
    if p2 not in choices:
        print('Input has to be either 1, 2 or 3')
        continue

    if p1 == p2:
        print('tie!')
    
    if choices.index(p1) == (choices.index(p2) + 1 ) % 3:
        print("Player 2 wins")
    if choices.index(p2) == (choices.index(p1) + 1 ) % 3:
        print('Player 1 wins')