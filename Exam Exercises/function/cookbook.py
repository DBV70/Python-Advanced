def cookbook(*args):
    cuisines = {}

    for recipe, cuisine, ingredients in args:
        if cuisine not in cuisines:
            cuisines[cuisine] = []
        cuisines[cuisine].append((recipe, ingredients))

    sorted_cuisines = sorted(cuisines.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for cuisine, recipes in sorted_cuisines:
        sorted_recipes = sorted(recipes, key=lambda x: x[0])
        result += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        for recipe_name, ingredients in sorted_recipes:
            result += f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n"

    return result.strip()

# Test code
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))