def classify_books(*args, **kwargs):
    library = {
        "fiction": [],
        "non_fiction": []
    }

    for book_type, book_title in args:
        isbn = next((key for key, value in kwargs.items() if value == book_title), None)
        library[book_type].append((isbn, book_title))

    result = ''
    if library["fiction"]:
        sorted_fiction = sorted(library["fiction"], key=lambda x: x[0])
        result += f"Fiction Books:\n"
        for isbn, title in sorted_fiction:
            result += f"~~~{isbn}#{title}\n"

    if library["non_fiction"]:
        sorted_non_fiction = sorted(library["non_fiction"], reverse=True, key=lambda x: x[0])
        result += f"Non-Fiction Books:\n"
        for isbn, title in sorted_non_fiction:
            result += f"***{isbn}#{title}\n"

    return result.strip()

# Test code
# print(classify_books(
#     ("fiction", "Brave New World"), ("non_fiction", "The Art of War"),
#     NF3421NN="The Art of War",FF1234UU="Brave New World"
# ))
# print(classify_books(
#     ("non_fiction", "The Art of War"),
#     ("fiction", "The Great Gatsby"),
#     ("non_fiction", "A Brief History of Time"),
#     ("fiction", "Brave New World"),
#     FF1234HH="The Great Gatsby",
#     NF3845UU="A Brief History of Time",
#     NF3421NN="The Art of War",
#     FF1234UU="Brave New World"
# ))
# print(classify_books(
#     ("fiction", "Brave New World"),
#     ("fiction", "The Catcher in the Rye"),
#     ("fiction", "1984"),
#     FICCITRZZ="The Catcher in the Rye",
#     FIC1984XX="1984",
#     FICBNWYYY="Brave New World"
# ))
# print(classify_books(
#     ("non_fiction", "Sapiens"),
#     ("non_fiction", "Homo Deus"),
#     ("non_fiction", "The Selfish Gene"),
#     NF123ABC="Sapiens",
#     NF987XYZ="Homo Deus",
#     NF456DEF="The Selfish Gene"
# ))
