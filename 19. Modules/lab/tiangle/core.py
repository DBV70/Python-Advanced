def print_upper_part(n):
    for row in range(1, n + 1):
        for num in range(1, row + 1):
            print(num, end=" ")
        print()

def print_lower_part(n):
    for row in range(n, 0, -1):
        for num in range(1, row):
            print(num, end=" ")
        print()

def print_triangle(n):
    print_upper_part(n)
    print_lower_part(n)