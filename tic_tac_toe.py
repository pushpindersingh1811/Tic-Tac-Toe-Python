import random
import pyautogui


board = [' ']*10
available = [str(num) for num in range(0, 10)]
players = [0, 'X', 'O']


def theboard(b, a):
    print('AVAILABLE      TIC TAC TOE\n' +
          'MOVES\n' +
          a[7] + '|' + a[8] + '|' + a[9] + '        ' + b[7] + '|' + b[8] + '|' + b[9] + '\n' +
          '-----        -----\n' +
          a[4] + '|' + a[5] + '|' + a[6] + '        ' + b[4] + '|' + b[5] + '|' + b[6] + '\n' +
          '-----        -----\n' +
          a[1] + '|' + a[2] + '|' + a[3] + '        ' + b[1] + '|' + b[2] + '|' + b[3]

          )

def place_marker(board, available, marker, position):
    board[position] = marker
    available[position] = ' '

def player_choice(board,player):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        try:
            position = int(input(f'Player {player} will choose between (1-9)>> '))
        except:
            print('Sorry!! Please choose the correct option!!')
    else:
        return position

def space_check(board,position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board[1:]


def choose_first():
    return random.randint(-1, 1)

def win_check(board,mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark)

    )


def replay():
    return input('Do you want to play again. Press(Y/N)').lower().startswith('y')


while True:
    pyautogui.hotkey('ctrl', 'shift', 'o')
    print('  Welcome to TIC-TAC TOE\n')
    toggle = choose_first()
    player = players[toggle]
    print(f'So, Player {player} will go first!!')

    game_on = True

    input('Hit enter to get started!!')

    while game_on:
        theboard(board, available)
        position = player_choice(board,player)
        place_marker(board, available, player, position)

        if win_check(board,player):
            pyautogui.hotkey('ctrl', 'shift', 'o')
            theboard(board, available)
            print(f'Congradulations, Player {player} WINS!!!')
            game_on = False
        else:
            if full_board_check(board):
                pyautogui.hotkey('ctrl', 'shift', 'o')
                theboard(board, available)
                print('GAME TIED!!!')
                break
            else:
                toggle *= -1
                player = players[toggle]
                pyautogui.hotkey('ctrl', 'shift', 'o')

    board = [' ']*10
    available = [str(num) for num in range(0, 10)]

    if not replay():
        break


