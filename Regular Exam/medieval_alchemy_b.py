from collections import deque

substances = [int(x) for x in input().split(', ')]
crystals = deque(int(x) for x in input().split(', '))

potions = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength"
}
crafted_potions = {}

while substances and crystals and len(crafted_potions) < 5:
    substance = substances.pop()
    cristal = crystals.popleft()

    if substance + cristal in potions.keys():
        crafted_potions[substance + cristal] = potions[substance + cristal]
        potions.pop(substance + cristal)

    else:
        candidates = [x for x in potions.keys() if x < substance + cristal]
        if candidates:
            key = min(candidates, key=lambda x: (substance + cristal) - x)
            crafted_potions[key] = potions[key]
            potions.pop(key)
            crystals.append(cristal - 20) if (cristal - 20) > 0 else None
        else:
            crystals.append(cristal - 5) if (cristal - 5) > 0 else None

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions.values())}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in reversed(substances))}")
if crystals:
    print(f"Crystals: {', '.join(str(x) for x in crystals)}")

