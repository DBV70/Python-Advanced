n = int(input())
matrix = []
pos = [0, 0]
amount = 100

for i in range(n):
    matrix.append(list(input()))
    for j in range(n):
        if matrix[i][j] == "G":
            pos = [i, j]

def move(position, direction):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    dr, dc = moves[direction]
    return position[0] + dr, position[1] + dc

while True:
    command = input()
    if command == "end":
        print(f"End of the game. Total amount: {amount}$")
        break
    row, col = pos
    r, c = move(pos, command)
    if r < 0 or r >= n or c < 0 or c >= n:
        print(f"Game over! You lost everything!")
        break

    pos = [r, c]
    matrix[row][col] = "-"
    if matrix[r][c] == "W":
        amount += 100

    if matrix[r][c] == "P":
        amount -= 200
        if amount <= 0:
            print(f"Game over! You lost everything!")
            break

    if matrix[r][c] == "J":
        amount += 100000
        print(f"You win the Jackpot! End of the game. Total amount: {amount}$")
        break

matrix[r][c] = "G"
if amount > 0:
    for row in matrix:
        print(*row, sep="")