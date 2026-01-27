n = int(input())
nums = []

for _ in range(n):
    data = [int(el) for el in input().split(', ')]
    nums.extend(data)

print(nums)

