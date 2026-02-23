from collections import deque

pocket_money = [int(x) for x in input().split()]
food_prices = deque([int(x) for x in input().split()])
food_count = 0

while pocket_money and food_prices:
    money = pocket_money.pop()
    price = food_prices.popleft()
    if money < price:
        continue
    else:
        difference = money - price
        if pocket_money:
            pocket_money[-1] += difference
        else: pocket_money.append(difference)
        food_count += 1

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif food_count == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif food_count == 1:
    print("Henry ate: 1 food.")
else:
    print(f"Henry ate: {food_count} foods.")
