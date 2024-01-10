import random

# Board for the computer
HIDDEN_COMPUTER = [[' ~ '] *9 for x in range(9)]

# Board for the user. Here you will se misses and hits on the ships.
PLAYER_BOARD_SEEN = [[' ~ '] *9 for x in range(9)]

# Converting Letter to numbers
LETTER_TO_NUM = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8}


def welcome_instruction_name():
    '''
    Welcome message is desplayed and also some information about the game. 
    Player will start the game with tying in their name.
    '''
    print("-----------------------")
    print("Welcome to Battleships!")
    print("-----------------------\n")
    print("-Your task is to sink all 5 boats that are in the ocean")
    print("-The boats are randomly placed and can be 1-3 in lenght")
    print("-Guess a row (A - I) and a column (0 - 8)")
    print("-You will have 10 turns to complete the task")
    print("-To start the game enter your name\n")

    player_name = input("Please enter your name: ")

    print(f"Let's sink some boats {player_name}!")

welcome_instruction_name()



def create_board(board):
    '''
    Create board
    '''
    print("   A   B   C   D   E   F   G   H   I  ")
    print("  -----------------------------------")

    row_number = 1
    for row in board:
        print(f"{row_number}|{'|'.join(row)}|")
        row_number +=1

    print("  -----------------------------------")

create_board(PLAYER_BOARD_SEEN)



def create_ships():
    pass




def ship_hit():
    pass



def get_ships():
    pass



def game_battleship():
    pass

