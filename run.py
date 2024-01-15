import random

# Board for the computer
HIDDEN_COMPUTER = [[' ~ '] *9 for x in range(9)]

# Board for the user. Here you will se misses and hits on the ships.
PLAYER_BOARD_SEEN = [[' ~ '] *9 for x in range(9)]

# Converting Letter to numbers
LETTER_TO_NUM = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8}

SHIP_LENGTHS = [2, 3, 4, 5]


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
    print("-You will have 20 turns to complete the task")
    print("-To start the game enter your name\n")

    while True:
        player_name = input("Please enter your name: ")
        if player_name:
            break
        print("Name can not be empty, try again")
       


    print(f"Let's sink some boats {player_name}!")
    print("")

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




def create_ships(board):
    '''
    Prints the boats on the boards for both the player and the computer
    '''
    for ship_size in SHIP_LENGTHS:
        while True:
            if board == HIDDEN_COMPUTER:
                orientation = random.choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    row = random.randint(0, len(board) - 1)
                    column = random.randint(0, len(board) - ship_size)
                    for i in range(column, column + ship_size):
                        board[row][i] = ' S '  
                else:
                    row = random.randint(0, len(board) - ship_size)
                    column = random.randint(0, len(board) - 1)
                    for i in range(row, row + ship_size):
                        board[i][column] = ' S '
                break
   
        if board == PLAYER_BOARD_SEEN:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, len(board) - 1)
                column = random.randint(0, len(board) - ship_size)
                for i in range(column, column + ship_size):
                    board[row][i] = ' S '    
            else:
                row = random.randint(0, len(board) - ship_size)
                column = random.randint(0, len(board) - 1)
                for i in range(row, row + ship_size):
                    board[i][column] = ' S '
            break


def ship_hit():
    '''
    This functions counts the hits of both the player and the computer
    '''
    count = 0
    for row in board:
        for column in row:
            if column == ' S ':
                count += 1
    return count


def check_ship_fits(SHIP_LENGTHS, x, y, orientation):
    if orientation == ' S ':
        if x + SHIP_LENGTHS > 9:
            return False
        else:
             return True

    else:
        if y + SHIP_LENGTHS > 9:
            return False
        else:
            return True

def ship_overlaps(ship_size, row, column, orientation):
    if orientation == "horizontal":
        for i in range(column, column + ship_size):
            if board[i][row] == ' S ':
                return True
    else:
        for i in range(row, row + ship_size):
            if board[column][i] == ' S ':
                return True 
    return False


def player_input(create_board):
    '''
    Here the player types in their guesses for both rows and columns.
    They get and error message if they type in the wrong key and then they try again.
    '''
    while True:
        try:
            row = input("Guess the row between 1-9:\n")
            if row in "123456789":
                row = int(row) -1
                break

        except ValueError:
            print("Wrong row number, try again")

    while True:
        try:
            column = input("Guess the column between A-I:\n").upper()
            if row in "ABCDEFGHI":
                column = LETTER_TO_NUM[column]
                break

        except KeyError:
            print("Wrong column letter, try again")
    return row, column

def get_ships():
    pass



def game_battleship():
    pass
