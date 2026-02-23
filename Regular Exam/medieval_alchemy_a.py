from collections import deque

potions ={
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70
}
crafted_potions = {}

substances = [int(x) for x in input().split(', ')]
energy_crystals = deque(int(x) for x in input().split(', '))

while substances and energy_crystals and len(crafted_potions) < 5:
    substance = substances.pop()
    cristal = energy_crystals.popleft()

    for key, value in crafted_potions.items():
        if key in potions:
            potions.pop(key)

    if substance + cristal in potions.values():
        crafted_potions.update({key: substance + cristal for key, value in potions.items() if value == substance + cristal})
        continue

    for key, value in potions.items():
        if key not in crafted_potions and value < substance + cristal:
            crafted_potions[key] = value
            energy_crystals.append(cristal - 20) if (cristal -20) > 0 else None
            break
    else:
        energy_crystals.append(cristal - 5) if (cristal - 5) > 0 else None

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions.keys())}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in reversed(substances))}")
if energy_crystals:
    print(f"Crystals: {', '.join(str(x) for x in energy_crystals)}")
