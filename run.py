import random

# Board for the computer
HIDDEN_COMPUTER = [['( )'] *11 for x in range(11)]

# Board for the user. Here you will se misses and hits on the ships.
PLAYER_BOARD_SEEN = [['( )'] *11 for x in range(11)]

# Converting Letter to numbers
LETTER_TO_NUM = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10}


