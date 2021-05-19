from math import *

def players():
    print('Then to play a game we need to know who you are!')
    player_1 = input("What is player1's name? \n")
    player_2 = input("What is player2's name? \n")
    return (player_1, player_2)


grid = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
        ]

# Printing a grid
def tic_tac_toe(grid):
    for row in grid:
        for space in row:
            print(space, end="\t")
        print("\n")

# Selection a space from a grid
def games_on():
    is_right = False
    while is_right == False:
        choice = input('Please choose a cell... \n')
        if choice.isdigit():
            if int(choice) in range(1, 10):
                is_right = True
            else:
                print('You entered wrong number! ! !')
        else:
            print('You entered invalid value! ! !')
    return choice


# Marking spaces with marks
def mark_cell(grid, space, mark):
    nottaken = False

    row = ceil(int(space)/3)
    if int(space) % 3 == 0:
        column = 3
    else:
        column = int(space) % 3

    if grid[row-1][column-1] == space:
        nottaken = True
        grid[row-1][column-1] = mark
    else:
        print("Space is taken!")
    return nottaken


# Receiving players' permission to continue play a game
def player_choice(player):
    is_right = False
    while is_right == False:
        choice = input(f'Hey, {player}, do you want to keep playing this game? (Y,N)')
        if choice not in ['Y', 'N']:
            print("I can't understand you, try again...")
        else:
            is_right = True
    if choice == 'Y':
        return True
    elif choice == 'N':
        return False


# Checking results
def check_result(grid, mark):
    for row in grid:
        for space in row:
            if space != mark:
                break
        else:
            print("1")
            return True

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i] != mark:
                break
        else:
            print("2")
            return True

    for k in range(3):
        if grid[k][k] != mark:
            break
    else:
        print("3")
        return True

    for k in range(3):
        if grid[k][2-k] != mark:
            break
    else:
        print("4")
        return True

    return False


def checkDraw(grid, mark1, mark2):
    there_is_not_winner = False

    for item in grid[0]:
        if item == mark1 or item == mark2:
            there_is_not_winner = True
        else:
            there_is_not_winner = False
            return there_is_not_winner

    for item in grid[1]:
        if item == mark1 or item == mark2:
            there_is_not_winner = True
        else:
            there_is_not_winner = False
            return there_is_not_winner

    for item in grid[2]:
        if item == mark1 or item == mark2:
            there_is_not_winner = True
        else:
            there_is_not_winner = False
            return there_is_not_winner

    return there_is_not_winner

mark1 = 'X'
mark2 = 'O'

game_on = True

player1, player2 = players()

print("{}, your marker is {} and {}'s marker is {}".format(player1, mark1, player2, mark2))

choice_1 = True
choice_2 = True

while game_on:

    tic_tac_toe(grid)

    mark = False

    print(f'{player1}, please choose a cell.')

    while mark == False:
        space = games_on()
        mark = mark_cell(grid, space, mark1)

    tic_tac_toe(grid)

    there_is_winner_1 = check_result(grid, mark1)
    there_is_winner_2 = check_result(grid, mark2)
    draw = checkDraw(grid, mark1, mark2)

    if there_is_winner_1 == True:
        print(f'You win, {player1}')

    elif there_is_winner_2 == True:
        print(f'You win, {player2}')

    elif draw == True:
        print(f'In this game, neither {player1} nor {player2} win')

    if there_is_winner_1 or there_is_winner_2 or draw == True:
        choice_1 = player_choice(player1)
        choice_2 = player_choice(player2)

    if choice_1 == False or choice_2 == False:
        break

    mark = False

    print(f"{player2}, it's your turn.")

    while mark == False:
        space = games_on()
        mark = mark_cell(grid, space, mark2)

    there_is_winner_1 = check_result(grid, mark1)
    there_is_winner_2 = check_result(grid, mark2)
    draw = checkDraw(grid, mark1, mark2)

    if there_is_winner_1 == True:
        print(f'You win, {player1}')

    elif there_is_winner_2 == True:
        print(f'You win, {player2}')

    elif draw == True:
        print(f'In this game, neither {player1} nor {player2} win')

    if there_is_winner_1 or there_is_winner_2 or draw == True:
        choice_1 = player_choice(player1)
        choice_2 = player_choice(player2)

    if choice_1 == False or choice_2 == False:
        game_on = False