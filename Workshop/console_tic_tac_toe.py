from math import ceil
def setup():
    global player_one, player_two
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()
    while player_one_sign not in ['X', 'O']:
        print("Invalid input!")
        player_one_sign = input("Please choose either 'X' or 'O': ").upper()
    player_two_sign = 'X' if player_one_sign == 'O' else 'O'
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{player_one_name} starts first!")
def draw_board(board):
    for row in board:
        print(f"| {" | ".join(row)} |")
def check_if_won(current, board):
    global loop
    first_row = all([x == current[1] for x in board[0]])
    second_row = all([x == current[1] for x in board[1]])
    third_row = all([x == current[1] for x in board[2]])
    first_col = all(x == current[1] for x in [board[0][0], board[1][0], board[2][0]])
    second_col = all(x == current[1] for x in [board[0][1], board[1][1], board[2][1]])
    third_col = all(x == current[1] for x in [board[0][2], board[1][2], board[2][2]])
    first_diagonal = all(x == current[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current[1] for x in [board[2][0], board[1][1], board[0][2]])
    if any([first_row, second_row, third_row, first_col, second_col, third_col, first_diagonal, second_diagonal]):
        print(f"{current[0]} won!")
        loop = False
    elif turn >= 9:
        print("Thanks for playing, no winner today!")
        loop = False
def play(current, board):
    global turn
    while True:
        try:
            choice = int(input(f"{current[0]}, choose a free position [1-9]: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice not in range(1, 10):
            print("Please enter a valid number between 1 and 9!")
            continue

        row = ceil(choice / 3) - 1
        col = choice % 3 - 1
        if board[row][col] != " ":
            print("Position already taken!")
            continue

        board[row][col] = current[1]
        draw_board(board)
        turn += 1
        if turn >= 5:
            check_if_won(current, board)
        return

player_one = None
player_two = None
board = [[" ", " ", " "] for _ in range(3)]
setup ()
current = player_one
other = player_two
loop = True
turn = 0

while loop:
    play(current, board)
    current, other = other, current
