def draw_triangle(n):
    if n <= 0:
        return
    print("*" * n)
    draw_triangle(n - 1)
    print("#" * n)

number = int(input())
draw_triangle(number)