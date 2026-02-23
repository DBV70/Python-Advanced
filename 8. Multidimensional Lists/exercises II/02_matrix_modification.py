rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        for row in matrix:
            print(*row)
        break

    r, c, val = int(command[1]), int(command[2]), int(command[3])
    if 0 <= r < rows and 0 <= c < len(matrix[0]):
        if command[0] == 'Add':
            matrix[r][c] += val
        elif command[0] == 'Subtract':
            matrix[r][c] -= val
    else:
        print('Invalid coordinates')
