odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    curr_num = sum(ord(ch) for ch in input()) // row

    if curr_num % 2 == 0:
        even_set.add(curr_num)
    else:
        odd_set.add(curr_num)

if sum(odd_set) == sum(even_set):
    print(*even_set | odd_set, sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set - even_set, sep=", ")
else:
    print(", ".join(str(x) for x in even_set ^ odd_set))
