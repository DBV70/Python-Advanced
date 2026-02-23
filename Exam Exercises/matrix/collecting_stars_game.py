n = int(input())
matrix =[]
pos = [0, 0]
score = 2

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "P":
            pos = [row, col]

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    row, col = pos
    dr, dc = moves[command]
    r, c = row + dr, col + dc

    matrix[row][col] = "."
    if 0 <= r < n and 0 <= c < n:
        if matrix[r][c] == "#":
            score -= 1
            if score == 0:
                break
            continue

        pos = [r, c]
        if matrix[r][c] == "*":
            score += 1
            if score == 10:
                break
    else:
        r, c = 0, 0
        if matrix[r][c] == "*":
            score += 1
        pos = [r, c]

if score >= 10:
    print("You won! You have collected 10 stars.")
if score <= 0:
    print("Game over! You are out of any stars.")

matrix[pos[0]][pos[1]] = "P"
print(f"Your final position is {pos}")
[print(*row) for row in matrix]
