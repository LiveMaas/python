import os

def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal screen
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

#from IPython.display import clear_output

# def display_board(board):
#     clear_output()  # Remember, this only works in jupyter!
    
#     print('   |   |')
#     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#     print('   |   |')

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[7] == board[4] == board[1] == mark:
        return True
    elif board[8] == board[5] == board[2] == mark:
        return True
    elif board[9] == board[6] == board[3] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[7] == board[5] == board[3] == mark:
        return True
    return False

import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"
choose_first()

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    
    for i in board:
        if i == ' ':
            return False
    return True

def player_choice(board):
    next_position = 0
    valid_list = [1,2,3,4,5,6,7,8,9]
    while next_position not in valid_list:
        next_position = int(input("Enter your spot (1 - 9)"))          
        if space_check(board,next_position):
            return next_position
        else:
            print("Spot already used.")
            next_position = 0


def replay():
    replay_input = input("Play again (Yes,No)?")
    if replay_input == 'Yes':
        print("Game On!")
        return True
    print("Come back soon!")
    return False

print('Welcome to Tic Tac Toe!')
#while True: # Set the game up here

play = True 
while play: 
    marker_tuple = player_input() 
    player = choose_first() 
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
    display_board(board)

#print(player)
#while game_on:
    game_on = True
    while game_on:
        #print(game_on)
        if player == "Player 1":
            print(f"{player}'s turn. Marker - {marker_tuple[0]}")
            choice = player_choice(board)
            place_marker(board,marker_tuple[0],choice)
            display_board(board)
            if win_check(board,marker_tuple[0]):
                print(f"Congratulation {player} - You won!")
                break
            player = "Player 2"
        else:
            print(f"{player}'s turn. Marker - {marker_tuple[1]}")
            choice = player_choice(board)
            place_marker(board,marker_tuple[1],choice)
            display_board(board)
            if win_check(board,marker_tuple[1]):
                print(f"Congratulation {player} - You won!")
                break
            player = "Player 1"
               
        if full_board_check(board):
            print("Tie game.")
            game_on = False
    
    #if not replay():
    play = replay()