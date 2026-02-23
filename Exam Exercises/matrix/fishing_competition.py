n = int(input())
matrix = []
pos = [0, 0]
fish_count = 0
quota = 20

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "S":
            pos = [row, col]

def move(position, direction, mtrx):
    n = len(mtrx)
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    cr, cc = position
    dr, dc = moves[direction]
    nr = (cr + dr) % n
    nc = (cc + dc) % n
    return nr, nc

while True:
    command = input()
    if command == "collect the nets":
        break

    row, col = pos
    matrix[row][col] = "-"
    r, c = move(pos, command, matrix)
    pos = [r, c]
    if 0 <= r < n and 0 <= c < n:
        if matrix[r][c] == "W":
            fish_count = -1
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{r},{c}]")
            break

        if matrix[r][c].isdigit():
            fish_count += int(matrix[r][c])

if fish_count != -1:
    r, c = pos
    matrix[r][c] = "S"
    if fish_count >= quota:
        print(f"Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {quota - fish_count} tons of fish more.")

    if fish_count > 0:
        print(f"Amount of fish caught: {fish_count} tons.")

    [print(''.join(row)) for row in matrix]