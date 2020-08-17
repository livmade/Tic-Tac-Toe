'''
  _____   _   ______    _____     __      ______    _____   _______    ______
 |_   _| | | |   ___|  |_   _|   /  \    |   ___|  |_   _| |   _   |  |   ___|
   | |   | | |  |        | |    / || \   |  |        | |   |  | |  |  |  |___
   | |   | | |  |        | |   /  __  \  |  |        | |   |  | |  |  |   ___|
   | |   | | |  |___     | |  /  /  \  \ |  |___     | |   |  |_|  |  |  |___
   | |   | | |      |    | | /  /    \  \|      |    | |   |       |  |      |
   ---   ---  ------     --- ---      --- ------     ---    -------    -------

'''
import random
from os import system,name

#     Functions for the gameplay    #

# Functions for the board:
def display_board(board): #Function creates board and gameplay spaces
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def win_check(board,mark): #Checks for Tic-Tac-Toe Wins
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def place_marker(board, marker, move): #Marker position
    board[move] = marker

def full_board_check(board): # Checks to see if board is full
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def space_check(board, move): # Checks if space is availble
    return board[move] == ' '

def players(): # Allowing players to select X or O
    character = ''
    while character not in ('X','O'):
        character = input("Pick your character: X or O.\n").upper()
    if character == 'X':
        human = 'X'
        comp = 'O'
        return (human, comp)
    else:
        human = 'O'
        comp = 'X'
        return(human,comp)

def player_order(): # Randomly selects CPU or player to go first
    if random.randint(0,1) == 0:
        print('The computer will go first.\n')
        return 'CPU'
    else:
        print('You will go first.\n')
        return 'Player 1'

def player_move(board): # Player move function
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(move)):
        move = input("Select a number between 1 - 9: ")
    return int(move)

def cpu_move(board): # CPU move function
    print('CPU\'s turn.')
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(move)):
        move = str(random.randint(0,8))
    return int(move)


# Gameplay Code
gameBoard = [' '] * 10
begin_game = ''
while begin_game not in ('Y','N'):
    begin_game = input("Do you want to play? Y/N\n")
    begin_game = begin_game.upper()
    if begin_game not in ('Y','N'):
        print("Invalid Selection\n")
    else:
        pass
print('\n Welcome!\n')

player_marker, cpu_marker = players()
whoseTurn = player_order()
gameOn = True

# Start gameplay:
while gameOn:
   if whoseTurn == 'Player 1':
       # Player's turn:
       display_board(gameBoard)
       move = player_move(gameBoard)
       place_marker(gameBoard, player_marker, move)

       if win_check(gameBoard, player_marker):
           display_board(gameBoard)
           print('Congratulations! You have won the game!')
           gameOn = False
       else:
            if full_board_check(gameBoard):
                display_board(gameBoard)
                print('The game is a draw!')
                break
            else:
                whoseTurn = 'CPU'
   else:
       # CPU's turn.
       display_board(gameBoard)
       move = cpu_move(gameBoard)
       place_marker(gameBoard, cpu_marker, move)

       if win_check(gameBoard, cpu_marker):
           display_board(gameBoard)
           print('The CPU has won!')
           gameOn = False
       else:
           if full_board_check(gameBoard):
               display_board(gameBoard)
               print('The game is a tie!')
               break
           else:
               whoseTurn = 'Player 1'
