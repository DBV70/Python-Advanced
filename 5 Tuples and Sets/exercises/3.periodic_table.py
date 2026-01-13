#elements = set()

#for _ in range(int(input())):
#    for el in input().split():
#        elements.add(el)

#for el in range(int(input())):
#    elements = elements.union(set(input().split()))

#print(*elements, sep="\n")

print(*{el for _ in range(int(input())) for el in input().split()}, sep="\n")
