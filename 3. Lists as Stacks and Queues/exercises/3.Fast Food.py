from collections import deque

food_qty = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders and orders[0] <= food_qty:
    food_qty -= orders.popleft()

if orders:
    print(f"Orders left:", *orders)
else:
    print("Orders complete")

