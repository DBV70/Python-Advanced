rows = int(input())
matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(data)

print(matrix)

# matrix_a = [[int(x) for x in input().split(', ') if int(x) % 2 == 0] for _ in range(int(input()))]
# print(matrix_a)
