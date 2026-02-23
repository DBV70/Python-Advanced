class MatrixSizeError(Exception):
    pass
class MatrixContentError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i + 1, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()



mtrx = []
while True:
    line = input().split()
    if not line:
        break
    row = line
    for n in line:
        # only positive digit
        # if not n.isdigit():
        #     raise MatrixContentError("The matrix must consist of only integers")
        try:
            int(n)
        except ValueError:
            raise MatrixContentError("The matrix must consist of only integers")
    mtrx.append(line)

rows = len(mtrx)
cols =  len(mtrx[0])
if rows != cols:
    raise MatrixSizeError("The size of the matrix is not a perfect square")

for row in mtrx:
    if len(row) != cols:
        raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)
for row in mtrx: print(*row, sep=' ')

# 1 2 3
# 4 5 6
# 7 8 9

# 1 2 3 4
# 5 6 7 8

# 7 8
# 9 k