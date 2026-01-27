n = int(input())
matrix = []
primary = []
secondary = []

for i in range(n):
    data = [int(el) for el in input().split(', ')]
    matrix.append(data)
    primary.append(data[i])
    secondary.append(data[n - i -1])

print(f'Primary diagonal: {", ".join(str(x) for x in primary)}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary )}. Sum: {sum(secondary)}')

# n = int(input())
# matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
# primary_diagonal = [matrix[i][i] for i in range(n)]
# secondary_diagonal = [matrix[n - i - 1][i] for i in range(n)]
#
# print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
# print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal )}. Sum: {sum(secondary_diagonal)}')
