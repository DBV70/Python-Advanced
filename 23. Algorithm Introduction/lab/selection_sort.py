def selection_sort(numbers):
    for idx in range(len(numbers)):
        min_idx = idx
        for j in range(idx + 1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

    return numbers

nums = [int(x) for x in input().split()]
print(*selection_sort(nums))