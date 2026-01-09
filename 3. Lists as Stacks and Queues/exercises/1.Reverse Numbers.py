from collections import deque
numbers = deque(map(int, input().split()))
print(*reversed(numbers))
