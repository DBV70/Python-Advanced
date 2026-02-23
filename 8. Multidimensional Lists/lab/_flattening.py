matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix for num in sublist]
print(flattened)

flattened = []
for sublist in matrix:
    for num in sublist:
        flattened.append(num)

print(flattened)
