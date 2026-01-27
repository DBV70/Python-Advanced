n = int(input())
matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

searched_symbol = input()

for i in range(n):
    for j in range(n):
        if matrix[i][j] == searched_symbol:
            print(f"({i}, {j})")
            exit()

print(f"{searched_symbol} does not occur in the matrix")
