def fill_the_box(h, l, w, *args):
    box_volume = h * l * w
    for i in range(len(args) - 1):
        if args[i] == "Finish":
            break
        box_volume -= args[i]
    if box_volume <= 0:
        return f"No more free space! You have {abs(box_volume)} more cubes."
    return f"There is free space in the box. You could put {box_volume} more cubes."

# test code
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))