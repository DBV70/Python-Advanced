def bubble_sort(numbers):
    is_sorted = False
    sorted_el = 0
    while not is_sorted:
        is_sorted = True
        for j in range(1, len(numbers) - sorted_el):
            i = j - 1
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                is_sorted = False
        sorted_el += 1
    return numbers

nums = [int(x) for x in input().split()]
print(*bubble_sort(nums))