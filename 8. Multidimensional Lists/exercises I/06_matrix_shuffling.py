r, c = map(int, input().split())
matrix = [[x for x in input().split()] for _ in range(r)]

command = input().split()
while command[0] != "END":
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
    else:
        r1, c1, r2, c2 = [int(x) for x in command[1:]]
        if r1 < 0 or r1 >= r or c1 < 0 or c1 >= c or r2 < 0 or r2 >= r or c2 < 0 or c2 >= c:
            print("Invalid input!")
        else:
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for i in range(r):
                print(*matrix[i])
    command = input().split()
