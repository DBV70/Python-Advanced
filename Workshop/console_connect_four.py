def play(player, board):
    global turn
    while True:
        try:
            choice = int(input(f"{player[0]}, please choose a column: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice not in range(1, len(board[0]) + 1):
            print(f"Please enter a valid column between 1 and {len(board[0])}!")
            continue

        if board[0][choice - 1] != 0:
            print("Column is full!")
            continue

        col = choice - 1
        for row in range(len(board) - 1, -1, -1):
            if board[row][col] == 0:
                board[row][col] = player[1]
                break

        [print(row) for row in board]
        turn += 1
        if turn >= 7:
            check_win(current, board)
        return

def check_win(player, board):
    global loop
    rows = len(board)
    cols = len(board[0]) if rows else 0
    # Check for streak in a row
    for r in range(rows):
        for c in range(cols - 3):
            if all(board[r][c + i] == player[1] for i in range(4)):
                print(f"The winner is {player[0]}")
                loop = False
                return

    # # Check for streak in a column
    for c in range(cols):
        for r in range(rows - 3):
            if all(board[r + i][c] == player[1] for i in range(4)):
                print(f"The winner is {player[0]}")
                loop = False
                return

    # Check down-right diagonals
    for r in range(rows - 3):
        for c in range(cols - 3):
            if all(board[r + i][c + i] ==player[1] for i in range(4)):
                print(f"The winner is {player[0]}")
                loop = False
                return

    # Check down-left diagonals
    for r in range(rows - 3):
        for c in range(3, cols):
            if all(board[r + i][c - i] ==player[1] for i in range(4)):
                print(f"The winner is {player[0]}")
                loop = False
                return

board = [[0 for _ in range(7)] for _ in range(6)]
current = ['Player 1', 1]
other = ['Player 2', 2]
turns = len(board) * len(board[0])
turn = 0
loop = True

while loop:
    play(current, board)
    current, other = other, current
    if turns - turn == 0:
        print("No more turns left!")
        break
