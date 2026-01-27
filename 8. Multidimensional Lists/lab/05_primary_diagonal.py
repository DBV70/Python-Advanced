n = int(input())
matrix = []

for i in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)

diagonal_sum = 0
for index in range(n):
           diagonal_sum += matrix[index][index]

print(diagonal_sum)
