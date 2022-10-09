import random

test_board = ['#','X','O','X','O','X','O','X','O','X']

def display_board(board):
    print(board[7] + '|' + board[8] +'|' + board[9])
    print(board[4] + '|' + board[5] +'|' + board[6])
    print(board[1] + '|' + board[2] +'|' + board[3])

display_board(test_board)

def player_input():
    '''
    OUTPUT = (Player 1 marker, PLayer 2 marker)
    '''
    marker = ''
    while marker != 'X' and marker !='O':
        marker = input('Player1: Choose X or O').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player1_marker, player2_marker = player_input()

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ''


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or space_check(board, position):
        position = int(input('Choose position (1-9)'))
    return position

def replay():
    choice = input('PLay again? Enter Yes or No')
    return choice == 'Yes'


















