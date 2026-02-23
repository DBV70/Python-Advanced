def insertion_sort(numbers):
    for j in range(1, len(numbers)):
        for i in range(j, 0, -1):
            if numbers[i] < numbers[i - 1]:
                numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            else:
                break
    return numbers

nums = [int(x) for x in input().split()]
print(*insertion_sort(nums))