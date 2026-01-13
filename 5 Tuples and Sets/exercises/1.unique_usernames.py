users = set()

for _ in range(int(input())):
    users.add(input())

#for user in users:
#   print(user)

#print("\n".join(users))"

print(*users, sep="\n")