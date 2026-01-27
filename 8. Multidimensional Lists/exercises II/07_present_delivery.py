presents = int(input())
n = int(input())
matrix = []
santa = [0, 0]
nice_kids = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            nice_kids += 1

nice_kids_gifted = 0
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    row, col = santa[0] + moves[command][0], santa[1] + moves[command][1]
    if 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "V":
            nice_kids_gifted += 1
            presents -= 1
            matrix[row][col] = "-"
        elif matrix[row][col] == "C":
            for move in moves.values():
                new_r, new_c = row + move[0], col + move[1]
                if matrix[new_r][new_c] in "VX" and presents > 0:
                    if matrix[new_r][new_c] == "V":
                        nice_kids_gifted += 1
                    presents -= 1
                    matrix[new_r][new_c] = "-"

        matrix[santa[0]][santa[1]] = "-"
        santa = [row, col]
        matrix[row][col] = "S"

if presents <= 0 and nice_kids_gifted < nice_kids:
    print("Santa ran out of presents!")

[print(*row, sep=" ") for row in matrix]

if nice_kids - nice_kids_gifted > 0:
    print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_gifted} happy nice kid/s.")