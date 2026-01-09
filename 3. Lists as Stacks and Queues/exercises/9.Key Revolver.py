from collections import deque
bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(int(x) for x in input().split())
money = int(input())

while bullets and locks:

