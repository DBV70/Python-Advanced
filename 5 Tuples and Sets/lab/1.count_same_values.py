numbers = tuple(map(float, input().split()))
data = {}

for num in numbers:
    if num not in data:
        data[num] = numbers.count(num)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")